#!/usr/bin/env bash
# CI-equivalent checks for uniStemCourseSimulators that run here without Docker or a browser stack.
#
#   verify.sh [--frontend] [--list] [--log-dir DIR]
#
#   --frontend  also run the React app's lint, unit tests, production build and bundle scan. They run in
#               a Linux copy of frontend/ under ~/.cache/node-copies, so build output on the mount is not
#               touched and any node_modules there (possibly built on Windows) is ignored.
#   --list      print the steps and exit.
#
# Steps follow .github/workflows/ci.yaml. NOT run here: the frontend-e2e job's docker compose stack and
# its Playwright browser tests (host or CI only). Every step runs even if another fails; the exit status is
# 1 when any step did not pass. Full output of each step is kept in the log directory.
set -u

REPO="/workspace/uniStemCourseSimulators"
SKILLS="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
VENV="$HOME/.cache/venvs/courselab"
PY="$VENV/bin/python"
RUFF="$VENV/bin/ruff"
LOG="$HOME/.cache/courselab-verify/$(date +%Y%m%d-%H%M%S)"
FRONTEND=0
LIST=0

while [ $# -gt 0 ]; do
  case "$1" in
    --frontend) FRONTEND=1 ;;
    --list) LIST=1 ;;
    --log-dir) LOG="${2:?--log-dir needs a path}"; shift ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    *) echo "unknown option: $1 (try --help)" >&2; exit 2 ;;
  esac
  shift
done

export PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg NO_COLOR=1

if [ "$LIST" = 1 ]; then
  cat <<'EOF'
content      python tools/validate_content.py                  (repo root)
legacy       npm run test:legacy                               (repo root)
security     python tools/check_security.py                    (repo root)
ruff         ruff check --no-cache backend tools tests         (repo root)
pytest-root  python -m pytest tests -q -p no:cacheprovider     (repo root; about 4 min here)
pytest-api   python -m pytest -q -p no:cacheprovider           (backend/; about 70 s here)
frontend     --frontend only: npm ci in a copy, lint, test, build, check_security --bundle
not run      docker compose stack + Playwright end-to-end tests (host or CI only)
EOF
  exit 0
fi

mkdir -p "$LOG" || { echo "cannot create $LOG" >&2; exit 1; }
echo "logs: $LOG"

# Dedicated venv outside the repo, pinned exactly as CI pins it (requirements-dev + backend pins).
python3 -B "$SKILLS/workspace-dev-env/scripts/make_venv.py" uniStemCourseSimulators --name courselab --isolated \
  --requirements requirements-dev.txt --requirements backend/requirements.txt > "$LOG/venv.log" 2>&1 \
  || { echo "venv setup failed; see $LOG/venv.log" >&2; tail -n 15 "$LOG/venv.log" >&2; exit 1; }

# run_step NAME WORKDIR COMMAND...  -> $LOG/NAME.log and $LOG/NAME.status ("PASS|FAIL exit seconds")
run_step() {
  local name="$1" dir="$2" t0 rc
  shift 2
  t0=$(date +%s)
  (cd "$dir" && "$@") > "$LOG/$name.log" 2>&1
  rc=$?
  printf '%s %s %s\n' "$([ "$rc" = 0 ] && echo PASS || echo FAIL)" "$rc" "$(( $(date +%s) - t0 ))" > "$LOG/$name.status"
}

frontend_chain() {
  local fe="$HOME/.cache/node-copies/courselab-frontend" sig
  mkdir -p "$fe" || return 1
  rsync -a --delete --exclude node_modules --exclude dist --exclude playwright-report --exclude test-results \
    "$REPO/frontend/" "$fe/" || return 1
  sig="$(sha256sum "$REPO/frontend/package-lock.json" | cut -d' ' -f1)"
  if [ ! -d "$fe/node_modules" ] || [ "$(cat "$fe/.lock-stamp" 2>/dev/null)" != "$sig" ]; then
    echo "== npm ci (in $fe) =="
    (cd "$fe" && npm ci --no-audit --no-fund --loglevel=error) || return 1
    echo "$sig" > "$fe/.lock-stamp"
  fi
  echo "== npm run lint ==";  (cd "$fe" && npm run lint) || return 1
  echo "== npm test ==";      (cd "$fe" && npm test) || return 1
  echo "== npm run build =="; (cd "$fe" && npm run build) || return 1
  echo "== bundle scan =="
  "$PY" "$REPO/tools/check_security.py" --bundle "$fe/dist"
}

# Quick checks first, one after another.
run_step content  "$REPO" "$PY" tools/validate_content.py
run_step legacy   "$REPO" npm run test:legacy
run_step security "$REPO" "$PY" tools/check_security.py
run_step ruff     "$REPO" "$RUFF" check --no-cache backend tools tests

# The slow suites in parallel (they only read the content tree and use temporary databases).
run_step pytest-root "$REPO"         "$PY" -m pytest tests -q -p no:cacheprovider &
run_step pytest-api  "$REPO/backend" "$PY" -m pytest -q -p no:cacheprovider &
[ "$FRONTEND" = 1 ] && run_step frontend "$REPO" frontend_chain &
wait

headline() {
  local log="$LOG/$1.log"
  case "$1" in
    content)  grep '^WARNING' "$log" | sed 's/; use --json.*//' | paste -sd' ' | sed 's/^/warnings: /' ;;
    legacy)   grep -E '^ℹ (tests|pass|fail) ' "$log" | tr -s ' ' | paste -sd' ' ;;
    pytest-*) grep -E '[0-9]+ (passed|failed|error)' "$log" | tail -n 1 ;;
    *)        grep -v '^$' "$log" | tail -n 1 ;;
  esac
}

overall=0
printf '\n%-12s %-6s %6s  %s\n' step result secs headline
for name in content legacy security ruff pytest-root pytest-api frontend; do
  [ -f "$LOG/$name.status" ] || { [ "$name" = frontend ] && [ "$FRONTEND" = 0 ] && printf '%-12s %-6s %6s  %s\n' frontend SKIP - "not requested (add --frontend)"; continue; }
  read -r res rc secs < "$LOG/$name.status"
  [ "$res" = PASS ] || overall=1
  printf '%-12s %-6s %6s  %s\n' "$name" "$res" "$secs" "$(headline "$name")"
  if [ "$res" != PASS ]; then
    echo "  last lines of $LOG/$name.log:"
    tail -n 12 "$LOG/$name.log" | sed 's/^/    | /'
  fi
done
echo
echo "not run here: docker compose stack and Playwright e2e (host or CI only)."
echo "full logs: $LOG"
exit "$overall"

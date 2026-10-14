# Running and deploying uniStemCourseSimulators

The default configuration runs a local learning system. `compose.production.yaml` is an operator example with Caddy HTTPS; it is not evidence of a public deployment or production security review. [VALIDATION_REPORT.md](VALIDATION_REPORT.md) records the checks actually performed. Courses remain partial, and the current server gradebook contains formative practice results only.

## Local startup

Install Docker Engine or Docker Desktop with the Compose plugin, then run from the repository root:

```sh
docker compose up --build
```

Open `http://localhost:8080`. No `.env` file, manually chosen database password or provider credential is needed. The `credentials` initialization service generates separate random bootstrap and API passwords in a named volume. A one-shot `db-roles` service provisions `courselab_app` with table/sequence data access but no schema-creation or role/database-administration rights; `migrate` uses the bootstrap account, and the API starts with only the runtime account after migration success. PostgreSQL starts on an internal Docker network, and nginx serves the compiled React application and proxies `/api/` to FastAPI. Only the web port is published, bound to loopback. A catalog/lesson can be read without an account; a guest or registered account is needed for persisted enrollment, attempts, notes and progress.

The database and credentials volumes persist across container recreation. Stop the foreground run with Ctrl+C, or use `docker compose down` after a detached run. Keep the volumes when learner records are needed. Removing a volume destroys its stored data; deleting only the credentials volume leaves the existing PostgreSQL password inconsistent with a newly generated secret. PostgreSQL initialization variables do not rotate an existing cluster's password.

Optional local configuration comes from `.env.example`; copy it to an untracked `.env` and edit only what is needed. If `COURSELAB_PORT` changes, update `ALLOWED_ORIGINS` to the exact matching localhost/127.0.0.1 origins. Development uses `COOKIE_SECURE=false` for local HTTP. The per-peer mutation limits default to 120 ordinary writes and 30 authentication writes per rolling minute; `COURSELAB_RATE_LIMIT` and `COURSELAB_AUTH_RATE_LIMIT` override them for Compose. CI uses higher values only for its disposable end-to-end test stack. No email allowlist grants review access; registration cannot assign roles. After verifying an instructor's identity and review authority out of band, an operator can provision the role from the API container using the user ID shown by `/api/v1/auth/session`:

```sh
docker compose exec -T api python -m courselab.manage_instructor USER_ID grant
docker compose exec -T api python -m courselab.manage_instructor USER_ID revoke
```

The `.env` files, secrets, database files, backups and learner exports are excluded from Git, but an ignore rule is not a substitute for inspecting staged changes.

## Assessment protection: open or protected

Protecting graded assessments is a choice, not a requirement. A course declares it in its manifest as `grading_policy.assessment_protection`, and an operator can force it for every course with the `ASSESSMENT_PROTECTION` environment variable.

| Value | Meaning |
| --- | --- |
| `open` (default) | A graded assessment may read its questions and keys from the public package. Anyone with the repository can read the answers, so a graded result depends on the learner's honesty. This suits self-directed study, where the aim is feedback, not certification. The API reports `assessment_protection: "open"` in the assessment plan so the interface can say so. |
| `protected` | Every graded assessment must read from the private store (`private://` sources, below). A public source is refused when the plan is built and again when questions are served, so switching a live deployment to protected closes any open graded assessment instead of leaving it exposed. |

`ASSESSMENT_PROTECTION` accepts `course` (default, defer to each course), `protected` or `open`. Practice and self-assessment items are public in both modes; protection concerns graded assessments only. Protection does not make an assessment secure by itself: it removes the answers from the repository, nothing more. No current package has a graded assessment.

## Protected assessment content

Production answer specifications belong in a separate private directory, never in the public `content/` tree, a frontend bundle, or a Git commit. Compose mounts `COURSELAB_PRIVATE_ASSESSMENTS_PATH` read-only at `/run/private-assessments`; the API resolves `private://` assessment sources below `courses/<course-id>/` in that mount. For example, a manifest source `private://assignments/homework-02.json` maps to `courses/cell-biology/assignments/homework-02.json` under the configured host directory. The public learner APIs omit source paths and grader specifications. Enrollment pins the source-file checksum; a missing or changed key fails closed instead of silently grading with different content. When the plan is pinned, exact graded source bytes are copied into the private `assessment_source_archives` database table so instructors can review historical submissions after files or course versions change. The API never returns those bytes; it returns only verified, answer-free question views to an authorized reviewer.

Development Compose defaults to the ignored `.local/private-assessments/` directory and creates it if needed. Production Compose defaults to `/srv/courselab-private-assessments`; set `COURSELAB_PRIVATE_ASSESSMENTS_PATH` in the untracked production environment file to an operator-controlled directory outside the checkout. The directory and JSON packages must be readable by the API container's uid 10001 and must not be writable by the service. PostgreSQL now also contains exact graded-source archives, including grader keys. Protect and encrypt database backups to the same standard as the private assessment directory, and include them in the answer-key retention policy. Do not put real answer files in the public repository, even temporarily or on a branch.

No current catalog course references a private graded package; all course packages remain formative-only. A course manifest must not switch to a graded policy until its assignment instructions, private question package, rubric, schedule, release policy, tests, and review are ready. When a manifest does reference a private source, the assessment-plan endpoint returns a conflict while that source is unavailable.

Appeal adjustments/upheld decisions are permitted only while the exact archived question source, resolved variant and saved digest match. New graded plans archive sources; Alembic 0010 does not backfill existing submissions, so those appeals can only be declined if their original source is unavailable. Full historical archives for course readings and other content remain future work. See [PROGRESS_REVIEW.md](PROGRESS_REVIEW.md) and [SECURITY.md](../SECURITY.md).

Useful diagnostics:

```sh
docker compose ps
docker compose logs --tail=100 migrate api web
docker compose exec -T api python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/api/v1/health').status)"
```

The health endpoint checks database connectivity; it is not an assessment-quality, security or full learner-workflow certification. Do not enable SQL parameter logging or log request bodies containing passwords, notes or learner responses.

## Product rename and existing data

Fresh checkouts use the Compose project name `uni-stem-course-simulators` (production: `uni-stem-course-simulators-production`). Compose normally prefixes volumes with that identity. A new name would select new empty volumes and make existing records appear missing.

Before upgrading an existing installation, record its project identity from `docker compose ls` and volume attachments from `docker inspect`. Back up and verify the database using the procedure below. Set `COMPOSE_PROJECT_NAME` to that **existing identity** in the deployment's untracked environment file; it overrides the new default `name`.

Preserve both the database and credentials volumes. Do not remove volumes, regenerate an existing database password or start a second writer against the same PostgreSQL volume. The current local installation retains its identity through this untracked setting. Renaming the underlying volumes is unnecessary for the product rename; a later volume migration requires a verified database backup and controlled restore/cutover.

The legacy reader writes to `uni-stem-course-simulators:guest:v3`. On the same browser origin it reads the most recent valid previous notebook, sanitizes/copies it, records its source key, and retains all old keys/backups. These old strings remain only as compatibility identifiers. Browser data remains unverified and is never imported as server grades. The database name, Python module, session cookie and `COURSELAB_*` environment variables stay stable technical identifiers to avoid unrelated session/database/configuration changes. New UI, exports, package names and metadata use the new identity. Existing Git checkouts can update their remote with:

```sh
git remote set-url origin https://github.com/dylanstechmann/uniStemCourseSimulators.git
```

## Database migration procedure

The API does not automatically create tables through ORM metadata. Alembic's versioned revisions are the deployment boundary. From a running local setup:

```sh
docker compose exec -T api alembic current
docker compose run --rm migrate
```

The second command runs `alembic upgrade head` using the same image and database as the API but the separate bootstrap password. The API uses `courselab_app`; the bootstrap account owns the schema and remains available for migrations and recovery. `db-roles` reapplies runtime grants before migrations, including default grants for tables/sequences created by future migrations. Revisions 0002–0004 add question digests, learner appeals and operator-provisioned instructor roles; revision 0010 adds private graded-source archives for new assessment plans and does not backfill older submissions, while 0011 archives public course packages on new enrollment and version upgrades. Old attempts are preserved and marked unpinned. For an application update, take and verify a backup, stop API/web writes, build the reviewed version, apply its migrations, and restart the application. Read each migration before applying it to valuable data. A downgrade is not a general data-recovery mechanism; some future changes may be irreversible. Upgrade/downgrade and migrated-schema comparisons are covered by backend tests.

Public content is copied into the API image at `/content`; protected assessment packages are mounted separately at `/run/private-assessments`. Rebuild when public course packages change. Enrollments record their course version; a changed version blocks version-dependent operations until the learner uses the explicit `PUT /api/v1/enrollments/{course_id}/version` action. This updates the enrollment pointer and preserves earlier attempts with their original course version. Do not rewrite published content under an unchanged version to bypass that boundary.

### Backfill legacy public course archives

Migration 0011 does not invent snapshots for existing enrollments. An operator can archive an old enrollment only when the exact public package bytes associated with that course release are independently known. A matching version string alone is insufficient because older deployments did not reject same-version file edits. The command is report-only by default and reports package digests without learner IDs:

```sh
docker compose exec -T api python -m courselab.backfill_course_archives --course-id cell-biology
```

Compare `package_sha256` with an independently retained, trusted release artifact or deployment record. Do not approve a digest merely because it appeared in this report. If the bytes match the verified release and the report says `digest_approval_required`, pass that independent digest to the write command:

```sh
EXPECTED_PACKAGE_SHA256=REPLACE_WITH_VERIFIED_64_HEX_DIGEST
docker compose exec -T api python -m courselab.backfill_course_archives --apply --course-id cell-biology --expected-package-sha256 "$EXPECTED_PACKAGE_SHA256"
```

For production, prefix both commands with `docker compose --env-file .env.production -f compose.production.yaml`. Take a verified database backup first. The command writes only public package archives and requires an exact current-version and digest match; it skips unavailable older versions and fails on a digest mismatch. If the original package cannot be verified, leave that enrollment unarchived rather than presenting current files as historical content.

To inspect saved graded-submission source coverage, run this strictly read-only aggregate audit:

```sh
docker compose exec -T api python -m courselab.audit_graded_archives
```

The report groups by course, pinned version, assessment and source-archive status. `source_archive_verified` means the saved links and archived source SHA-256 agree; it does not certify the answer key, grading result or academic quality. The report omits learner/submission identifiers, responses, scores and source text; it does not restore or infer missing historical content.

## Production example, domain and HTTPS

Use a host with Docker/Compose, a DNS hostname controlled by the operator, and network access suitable for certificate issuance. Set the hostname's A/AAAA records to that host, permit inbound TCP 80/443, and keep PostgreSQL/API ports unpublished. `COURSELAB_DOMAIN` must be the hostname alone, with no scheme, path or GitHub URL. The example does not depend on a particular cloud provider.

Create an untracked `.env.production` containing the intended `COURSELAB_DOMAIN`, absolute `DB_PASSWORD_FILE` and `DB_RUNTIME_PASSWORD_FILE` paths outside the checkout, a stable random `VARIANT_TOKEN_SECRET` of at least 32 bytes, and `COURSELAB_PRIVATE_ASSESSMENTS_PATH` pointing to a directory outside the checkout. Generate both database passwords only when initializing a new deployment; preserve them with the database volume. Keep the variant secret stable across API restarts so unexpired practice variant tokens remain usable. A Linux host example below creates operator-private files readable by uid 10001, used by the API and role-provisioning job:

```sh
sudo install -d -m 0700 /srv/courselab-secrets
sudo sh -c 'umask 077; test ! -e /srv/courselab-secrets/db-password && openssl rand -base64 32 > /srv/courselab-secrets/db-password'
sudo sh -c 'umask 077; test ! -e /srv/courselab-secrets/db-runtime-password && openssl rand -base64 32 > /srv/courselab-secrets/db-runtime-password'
sudo chown 10001:10001 /srv/courselab-secrets/db-password /srv/courselab-secrets/db-runtime-password
sudo chmod 0440 /srv/courselab-secrets/db-password /srv/courselab-secrets/db-runtime-password
sudo install -d -o 10001 -g 10001 -m 0750 /srv/courselab-private-assessments
openssl rand -hex 32
```

Store the generated `openssl` output as `VARIANT_TOKEN_SECRET` in `.env.production`; set `COURSELAB_PRIVATE_ASSESSMENTS_PATH=/srv/courselab-private-assessments`; never commit either private assessment files or credentials.

Set `DB_PASSWORD_FILE=/srv/courselab-secrets/db-password` and `DB_RUNTIME_PASSWORD_FILE=/srv/courselab-secrets/db-runtime-password`. The bootstrap password initializes PostgreSQL and runs migrations; `courselab_app` uses the runtime password and has no superuser, database-creation, role-creation or schema-creation rights. It can read and change application rows, including private answer archives, so database access and backups still require strict protection; table grants do not implement row-level isolation. Run subsequent production Docker commands as the host administrator (using `sudo` where needed). File-backed Compose secrets use host file permissions; uid/gid/mode remapping is not supported for that form. [Docker Compose secrets](https://docs.docker.com/reference/compose-file/services/#secrets). Check runtime-secret readability as the API container user before starting; the following command reads without displaying the value:

```sh
docker compose --env-file .env.production -f compose.production.yaml config --quiet
docker compose --env-file .env.production -f compose.production.yaml build
docker compose --env-file .env.production -f compose.production.yaml run --rm --no-deps api python -c "from pathlib import Path; assert Path('/run/secrets/db-runtime-password').read_text().strip(); print('Runtime secret is readable')"
docker compose --env-file .env.production -f compose.production.yaml up -d
```

The production file is a standalone configuration: use `-f compose.production.yaml`, rather than combining it with development port/cookie settings. It has its own Compose project name and volumes. Its API enables secure cookies and accepts only `https://<COURSELAB_DOMAIN>` as the mutation origin. Caddy loads [deploy/Caddyfile](../deploy/Caddyfile), terminates HTTPS and proxies to nginx; nginx routes API requests internally. Preserve Caddy's data/config volumes for certificate state. Caddy's public certificate automation depends on its documented DNS and reachability requirements. [Caddy automatic HTTPS](https://caddyserver.com/docs/automatic-https).

Production Compose applies CPU and memory caps to PostgreSQL (2 CPUs/2 GiB), API (1 CPU/1 GiB), migrations (1 CPU/2 GiB), nginx (0.5 CPU/128 MiB), and Caddy (0.5 CPU/256 MiB). API, database and migration limits can be changed with `COURSELAB_*_CPUS` and `COURSELAB_*_MEMORY_LIMIT` in `.env.production`; web/proxy caps are fixed in this example. Treat these as initial bounds. Load-test the expected concurrent learner and database workload, inspect memory/CPU throttling and PostgreSQL behavior, then tune before opening a deployment to learners.

Inspect service status, certificate errors and the learner workflow over HTTPS before opening the service to learners. If using a custom port or another proxy, deliberately update allowed origins and trusted forwarding configuration. HTTPS cookies will not work over plain HTTP. Password rotation must update PostgreSQL's actual role password and the mounted secret together; changing a file alone does not rotate an existing database. Plan rotation and session revocation without putting secret values in shell history or logs.

## Backup

Learner exports are not a database backup. Keep encrypted, access-controlled, off-host backups of PostgreSQL, the matching code/content version, migration revision and the private deployment configuration/secret needed for recovery. Database dumps contain learner records, password hashes, session records and exact graded assessment source archives with answer keys; handle them as highly restricted private data. A database dump does not include global role definitions or Caddy certificate volumes. Define retention and recovery objectives, and rehearse restoration on an isolated deployment.

The following commands use the **development** project and create a PostgreSQL custom-format archive. Create the ignored `backups/` directory first (`mkdir -p backups` in a POSIX shell, or `New-Item -ItemType Directory -Path backups -Force` in PowerShell). Use a unique filename for each backup, replacing the illustrative date below:

```sh
docker compose exec -T db pg_dump -U courselab -d courselab --format=custom --file=/tmp/courselab-backup.dump
docker compose exec -T db chmod 600 /tmp/courselab-backup.dump
docker compose cp db:/tmp/courselab-backup.dump backups/courselab-2026-10-05.dump
docker compose exec -T db rm /tmp/courselab-backup.dump
```

Inspect every command's exit status and dump warnings. Restrict permissions on the host copy and encrypt it before external storage. `docker compose cp` copies the binary archive directly; avoid PowerShell text redirection or text pipelines for custom-format dumps. In production, substitute `docker compose --env-file .env.production -f compose.production.yaml` for `docker compose` in each command. PostgreSQL documents the snapshot consistency and custom-archive behavior of [`pg_dump`](https://www.postgresql.org/docs/17/app-pgdump.html).

## Restore safely into a separate database

Use only a trusted archive from the intended deployment. Restore into a new database first, keeping the active `courselab` database unchanged. The commands below deliberately fail if `courselab_restore` already exists; choose a new recovery name instead of deleting an existing database to make the command pass.

```sh
docker compose cp backups/courselab-2026-10-05.dump db:/tmp/courselab-restore.dump
docker compose exec -T db pg_restore --list /tmp/courselab-restore.dump
docker compose exec -T db createdb -U courselab --template=template0 courselab_restore
docker compose exec -T db pg_restore -U courselab --dbname=courselab_restore --no-owner --no-privileges --exit-on-error --single-transaction /tmp/courselab-restore.dump
docker compose exec -T db psql -U courselab -d courselab_restore -c "SELECT version_num FROM alembic_version;"
docker compose exec -T db psql -U courselab -d courselab_restore -c "SELECT count(*) AS learner_count FROM users;"
docker compose exec -T db rm /tmp/courselab-restore.dump
```

Review the archive inventory before restoration. `--single-transaction` with `--exit-on-error` prevents a partially applied restore from being mistaken for success. `--no-owner --no-privileges` suits the current single-role deployment; when introducing least-privilege roles, restore ownership/grants through the reviewed role provisioning process. PostgreSQL explains these options and the execution of statements contained in trusted dumps in [`pg_restore`](https://www.postgresql.org/docs/17/app-pgrestore.html).

Run the matching application revision against the restored database in an isolated recovery configuration, inspect records, and exercise enrollment, lesson reading, submission, feedback and persisted progress. Do not expose restored learner data or restored sessions to the public during rehearsal. Plan a controlled maintenance cutover with writes stopped and a fresh backup. The example production file fixes the database name to `courselab`; a recovery override must set the API's `DB_NAME` to the restored name, and a reviewed migration/role plan must accompany any cutover. These commands document a recovery procedure; they do not assert that a public production recovery has been executed.

## Credential and execution boundaries

The application reads database credentials server-side from a secret file. `DATABASE_URL` overrides secret-file settings for tests or a deliberate operator configuration; it can contain a password and must never be printed or committed. The API uses hashed opaque session tokens, HttpOnly cookies, exact Origin/CSRF checks and application-level ownership filters. Learner data is stored in PostgreSQL; deleting browser storage is not server account deletion.

No provider credentials are required or supported by this milestone. LLM feedback and programming execution remain disabled. Future provider keys and restricted exam specifications need private server stores and disclosure policies. Neither the API nor the development containers should receive a Docker socket, host credential mount or arbitrary submission execution capability. The API image runs as uid 10001 with a read-only filesystem, dropped capabilities and a bounded temporary mount. Those controls do not constitute an isolated programming grader.

## Current hardening limits

Before public use, address the following concrete limitations of the example:

- PostgreSQL migration and API runtime accounts are split. `courselab_app` has no administrative or schema-creation rights and receives CRUD grants on current/future tables plus sequence access. Application ownership is still enforced by API queries; row-level security is not configured, and the runtime account can read/write every learner row and private answer archive.
- Mutation throttling is an in-memory single-worker limiter. Configure a shared production limiter, deliberate proxy trust and real-client attribution; the default network peer behind nginx is not a reliable per-learner identity.
- CPU/memory caps are configured in the production example, but capacity sizing and load tests remain operator work. Image digest pinning and operating-system image vulnerability checks also remain open. Python dependency audit results are in [backend/DEPENDENCY_AUDIT.md](../backend/DEPENDENCY_AUDIT.md).
- Email verification, password recovery, shared session administration, guest-data retention/cleanup, privacy procedures, monitoring and incident response require implementation or operator policy. Expired guest sessions do not currently clean up their learner records automatically.
- Concurrent unique-key writes return a safe 409 and need retry; atomic upserts and robust client retry policy remain to be implemented.
- The API container checks `/api/v1/health`, including its database query, and the production Compose example waits for API and web health before starting the next service. Local Compose validation reached PostgreSQL/API healthy and migration `0010 (head)`. This is a startup readiness check, not a full deployment health/rollback strategy. Automated backup scheduling and demonstrated recovery objectives remain operator work. The root validation report records development checks; it does not certify the public example.
- Restricted exams, protected exams, advanced graders, a validated code runner, full-course content gates and human course review remain roadmap work. Public seed practice specifications cannot protect a high-stakes exam.

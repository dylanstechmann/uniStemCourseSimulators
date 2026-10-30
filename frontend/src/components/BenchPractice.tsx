import { useEffect, useState } from "react";
import { api, errorMessage } from "../api";
import type {
  BenchAction,
  BenchActionSpec,
  BenchParam,
  BenchParamValue,
  BenchProtocol,
  BenchProtocolSummary,
  BenchRun,
} from "../types";

type Mode = "guided" | "practice";

function newSeed() {
  return Math.floor(Math.random() * 2_000_000_000);
}

function initialValue(param: BenchParam): BenchParamValue {
  if (param.type === "boolean") return false;
  if (param.type === "choice") return param.options?.[0]?.value ?? "";
  return "";
}

export function BenchPractice({ protocolId }: { protocolId?: string }) {
  const [protocols, setProtocols] = useState<BenchProtocolSummary[]>([]);
  const [error, setError] = useState("");
  useEffect(() => {
    api
      .benchProtocols()
      .then(setProtocols)
      .catch((reason) => setError(errorMessage(reason)));
  }, []);
  const selected =
    protocols.find((item) => item.id === protocolId) || protocols[0];
  return (
    <>
      <span className="eyebrow">Rehearse · decide · debrief</span>
      <h1>Bench practice</h1>
      <p className="lead">
        Rehearse real laboratory procedures before doing them at a bench. Choose
        each action yourself; the simulation keeps track of what a real bench
        would, including what you cannot see.
      </p>
      <p className="notice">
        Formative practice only. A run is not a grade, a competency record or a
        certification, and it cannot train hand skills. Follow your own
        laboratory&apos;s procedures and supervisors at a real bench.
      </p>
      {error && (
        <p className="error" role="alert">
          {error}
        </p>
      )}
      {protocols.length > 0 && (
        <nav className="tabs" aria-label="Bench protocols">
          {protocols.map((item) => (
            <a
              key={item.id}
              href={`#/bench/${encodeURIComponent(item.id)}`}
              aria-current={selected?.id === item.id ? "page" : undefined}
            >
              {item.title}
            </a>
          ))}
        </nav>
      )}
      {selected && <ProtocolRunner key={selected.id} id={selected.id} />}
    </>
  );
}

function ProtocolRunner({ id }: { id: string }) {
  const [protocol, setProtocol] = useState<BenchProtocol | null>(null);
  const [mode, setMode] = useState<Mode>("guided");
  const [seed, setSeed] = useState<number | null>(null);
  const [actions, setActions] = useState<BenchAction[]>([]);
  const [run, setRun] = useState<BenchRun | null>(null);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    api
      .benchProtocol(id)
      .then(setProtocol)
      .catch((reason) => setError(errorMessage(reason)));
  }, [id]);

  async function submit(next: BenchAction[], runSeed = seed, runMode = mode) {
    if (runSeed === null) return;
    setBusy(true);
    setError("");
    try {
      const result = await api.benchReplay(id, runSeed, runMode, next);
      setActions(next);
      setRun(result);
    } catch (reason) {
      setError(errorMessage(reason));
    } finally {
      setBusy(false);
    }
  }

  function start() {
    const fresh = newSeed();
    setSeed(fresh);
    void submit([], fresh, mode);
  }

  if (!protocol) {
    return error ? (
      <p className="error" role="alert">
        {error}
      </p>
    ) : (
      <p role="status">Loading protocol…</p>
    );
  }

  return (
    <section className="bench" aria-labelledby="bench-title">
      <div className="card">
        <h2 id="bench-title">{protocol.title}</h2>
        <p>{protocol.summary}</p>
        <p>
          <strong>Scenario.</strong> {protocol.scenario}
        </p>
        <div className="bench-start">
          <label>
            Mode{" "}
            <select
              value={mode}
              disabled={run !== null && !run.finished}
              onChange={(event) => setMode(event.target.value as Mode)}
            >
              <option value="guided">
                Guided: steps shown, mistakes flagged
              </option>
              <option value="practice">
                Practice: no prompts, consequences appear later
              </option>
            </select>
          </label>
          <button className="primary" onClick={start} disabled={busy}>
            {run ? "Start a new run" : "Start run"}
          </button>
        </div>
      </div>

      {error && (
        <p className="error" role="alert">
          {error}
        </p>
      )}

      {run && (
        <div className="bench-grid">
          <div>
            {run.guidance && (
              <section className="card">
                <h3>Procedure</h3>
                <ol>
                  {run.guidance.map((step) => (
                    <li key={step}>{step}</li>
                  ))}
                </ol>
              </section>
            )}
            <section className="card" aria-live="polite">
              <h3>
                Bench state{" "}
                <span className="muted">
                  (clock {run.clock_minutes.toFixed(1)} min)
                </span>
              </h3>
              {run.panels.map((panel) => (
                <table key={panel.title} className="bench-panel">
                  <caption>{panel.title}</caption>
                  <tbody>
                    {panel.rows.map(([label, value]) => (
                      <tr key={label}>
                        <th scope="row">{label}</th>
                        <td>{value}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              ))}
            </section>
          </div>
          <div>
            {!run.finished ? (
              <ActionForm
                specs={protocol.actions}
                busy={busy}
                onAct={(action) => void submit([...actions, action])}
              />
            ) : (
              <Debrief run={run} />
            )}
            {mode === "guided" && actions.length > 0 && !run.finished && (
              <button
                onClick={() => void submit(actions.slice(0, -1))}
                disabled={busy}
              >
                Undo last action
              </button>
            )}
            <RunLog run={run} />
          </div>
        </div>
      )}

      <section className="card">
        <h3>Limits of this simulation</h3>
        <ul>
          {protocol.limitations.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
        <p className="muted">
          Sources:{" "}
          {protocol.sources
            .map((source) => `${source.source_id} (${source.use})`)
            .join("; ")}
          . Listed in the source registry.
        </p>
      </section>
    </section>
  );
}

function ActionForm({
  specs,
  busy,
  onAct,
}: {
  specs: BenchActionSpec[];
  busy: boolean;
  onAct: (action: BenchAction) => void;
}) {
  const [name, setName] = useState(specs[0].name);
  const spec = specs.find((item) => item.name === name) || specs[0];
  const [values, setValues] = useState<Record<string, BenchParamValue>>(() =>
    Object.fromEntries(spec.params.map((p) => [p.name, initialValue(p)])),
  );
  const [problem, setProblem] = useState("");

  function choose(next: string) {
    const nextSpec = specs.find((item) => item.name === next) || specs[0];
    setName(next);
    setProblem("");
    setValues(
      Object.fromEntries(nextSpec.params.map((p) => [p.name, initialValue(p)])),
    );
  }

  return (
    <form
      className="card bench-action"
      noValidate
      onSubmit={(event) => {
        event.preventDefault();
        const params: Record<string, BenchParamValue> = {};
        for (const param of spec.params) {
          const value = values[param.name];
          if (param.type === "number" || param.type === "integer") {
            const number = Number(value);
            if (value === "" || !Number.isFinite(number)) {
              setProblem(`Enter a number for ${param.label.toLowerCase()}.`);
              return;
            }
            params[param.name] = number;
          } else {
            params[param.name] = value;
          }
        }
        setProblem("");
        onAct({ name: spec.name, params });
      }}
    >
      <h3>Next action</h3>
      <label>
        Action{" "}
        <select value={name} onChange={(event) => choose(event.target.value)}>
          {specs.map((item) => (
            <option key={item.name} value={item.name}>
              {item.label}
            </option>
          ))}
        </select>
      </label>
      {spec.params.map((param) => (
        <ParamInput
          key={`${spec.name}:${param.name}`}
          param={param}
          value={values[param.name]}
          onChange={(value) => setValues({ ...values, [param.name]: value })}
        />
      ))}
      {problem && (
        <p className="error" role="alert">
          {problem}
        </p>
      )}
      <button className="primary" type="submit" disabled={busy}>
        Do it
      </button>
    </form>
  );
}

function ParamInput({
  param,
  value,
  onChange,
}: {
  param: BenchParam;
  value: BenchParamValue;
  onChange: (value: BenchParamValue) => void;
}) {
  if (param.type === "boolean") {
    return (
      <label className="choice">
        <input
          type="checkbox"
          checked={value === true}
          onChange={(event) => onChange(event.target.checked)}
        />{" "}
        {param.label}
      </label>
    );
  }
  if (param.type === "choice") {
    return (
      <label>
        {param.label}{" "}
        <select
          value={String(value)}
          onChange={(event) => onChange(event.target.value)}
        >
          {param.options?.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </label>
    );
  }
  return (
    <label>
      {param.label}
      {param.unit ? ` (${param.unit})` : ""}{" "}
      <input
        type="number"
        inputMode="decimal"
        step={param.type === "integer" ? 1 : "any"}
        min={param.min}
        max={param.max}
        value={String(value)}
        onChange={(event) => onChange(event.target.value)}
      />
    </label>
  );
}

function RunLog({ run }: { run: BenchRun }) {
  if (!run.log.length) return null;
  return (
    <section className="card">
      <h3>What happened</h3>
      <ol reversed className="bench-log">
        {[...run.log].reverse().map((entry) => (
          <li key={entry.index}>
            <strong>{entry.label}</strong>{" "}
            <span className="muted">
              at {entry.clock_minutes.toFixed(1)} min
            </span>
            <ul>
              {entry.events.map((event, index) => (
                <li key={index} className={`bench-event-${event.kind}`}>
                  {event.kind === "warning" ? "Check: " : ""}
                  {event.kind === "consequence" ? "Result: " : ""}
                  {event.text}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ol>
    </section>
  );
}

function Debrief({ run }: { run: BenchRun }) {
  const debrief = run.debrief;
  if (!debrief) return null;
  const label = (met: boolean | null) =>
    met === null ? "Not applicable" : met ? "Met" : "Missed";
  return (
    <section className="card bench-debrief" aria-labelledby="debrief-title">
      <h3 id="debrief-title">Debrief</h3>
      <p>
        {debrief.met_count} of {debrief.applicable_count} applicable checkpoints
        met. Missed: {debrief.missed.critical} critical, {debrief.missed.major}{" "}
        major, {debrief.missed.minor} minor.{" "}
        {debrief.all_critical_met
          ? "Every critical checkpoint was met."
          : "At least one critical checkpoint was missed."}
      </p>
      {debrief.revealed.length > 0 && (
        <>
          <h4>What you could not see</h4>
          <ul>
            {debrief.revealed.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </>
      )}
      <table className="bench-checkpoints">
        <thead>
          <tr>
            <th scope="col">Checkpoint</th>
            <th scope="col">Severity</th>
            <th scope="col">Result</th>
          </tr>
        </thead>
        <tbody>
          {debrief.checkpoints.map((row) => (
            <tr key={row.id} className={`bench-met-${String(row.met)}`}>
              <td>
                <strong>{row.description}</strong>
                <br />
                {row.detail}
                <br />
                <span className="muted">
                  Why: {row.rationale}
                  {row.source.kind === "cited"
                    ? ` Source: ${row.source.source_id}, ${row.source.location}.`
                    : " Source: a typical value or model chosen for this simulation."}
                </span>
              </td>
              <td>{row.severity}</td>
              <td>{label(row.met)}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p className="muted">{debrief.note}</p>
    </section>
  );
}

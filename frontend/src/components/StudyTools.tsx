import { useState } from "react";
import { calculateStudyTool, studyTools } from "../studyTools";
import type { StudyTool, StudyToolResult } from "../studyTools";
import type { CourseSummary } from "../types";

export function StudyTools({
  toolId,
  courses,
}: {
  toolId?: string;
  courses: CourseSummary[];
}) {
  const selected =
    studyTools.find((tool) => tool.id === toolId) || studyTools[0];
  return (
    <>
      <span className="eyebrow">Explore · calculate · compare</span>
      <h1>Study tools</h1>
      <p className="lead">
        Explore the equations behind course examples. Check the units and
        assumptions, then change an input to see how the result responds.
      </p>
      <nav
        className="tabs study-tool-navigation"
        aria-label="Scientific calculators"
      >
        {studyTools.map((tool) => (
          <a
            key={tool.id}
            href={`#/tools/${tool.id}`}
            aria-current={selected.id === tool.id ? "page" : undefined}
          >
            {tool.title}
          </a>
        ))}
      </nav>
      <Calculator key={selected.id} tool={selected} />
      <section className="card">
        <h2>Related courses</h2>
        <ul>
          {selected.courseIds.map((id) => {
            const course = courses.find((item) => item.id === id);
            return course ? (
              <li key={id}>
                <a href={`#/course/${encodeURIComponent(id)}`}>
                  {course.title}
                </a>
              </li>
            ) : null;
          })}
        </ul>
      </section>
    </>
  );
}

function Calculator({ tool }: { tool: StudyTool }) {
  const defaults = () =>
    Object.fromEntries(tool.fields.map((field) => [field.id, field.initial]));
  const [input, setInput] = useState(defaults);
  const [result, setResult] = useState<StudyToolResult | null>(null);
  const [error, setError] = useState("");
  return (
    <section
      className="card study-calculator"
      aria-labelledby={`tool-${tool.id}`}
    >
      <h2 id={`tool-${tool.id}`}>{tool.title}</h2>
      <p>{tool.description}</p>
      <p className="tool-equation">
        <code>{tool.equation}</code>
      </p>
      <form
        noValidate
        onSubmit={(event) => {
          event.preventDefault();
          setError("");
          setResult(null);
          try {
            setResult(calculateStudyTool(tool, input));
          } catch (error) {
            setError(
              error instanceof Error ? error.message : "Check the inputs.",
            );
          }
        }}
      >
        <div className="input-grid">
          {tool.fields.map((field) => (
            <label key={field.id} htmlFor={`${tool.id}-${field.id}`}>
              {field.label}
              <input
                id={`${tool.id}-${field.id}`}
                type="number"
                step="any"
                min={field.minimum}
                required
                value={input[field.id]}
                onChange={(event) => {
                  setInput((previous) => ({
                    ...previous,
                    [field.id]: event.target.value,
                  }));
                  setResult(null);
                  setError("");
                }}
              />
            </label>
          ))}
        </div>
        <div className="actions">
          <button className="primary" type="submit">
            Calculate
          </button>
          <button
            type="button"
            onClick={() => {
              setInput(defaults());
              setResult(null);
              setError("");
            }}
          >
            Reset example
          </button>
        </div>
        {error && (
          <p role="alert" className="error">
            {error}
          </p>
        )}
        <div role="status" aria-live="polite">
          {result && (
            <dl className="tool-results">
              {result.map((item) => (
                <div key={item.label}>
                  <dt>{item.label}</dt>
                  <dd>
                    {Number(item.value.toPrecision(6)).toString()}
                    {item.unit ? ` ${item.unit}` : ""}
                  </dd>
                </div>
              ))}
            </dl>
          )}
        </div>
      </form>
      <h3>Model assumptions</h3>
      <p>{tool.assumptions}</p>
      <p className="muted">
        Calculator scratch work is not submitted or graded.
      </p>
    </section>
  );
}

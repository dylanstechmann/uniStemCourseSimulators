import { useEffect, useId, useState } from "react";
import { api, ApiError, errorMessage } from "../api";
import type { CaseDraft, CaseStudy, Course } from "../types";

function CaseEditor({
  courseId,
  version,
  study,
  draft,
  enabled,
  disabledMessage,
  onSaved,
  onReload,
}: {
  courseId: string;
  version: string;
  study: CaseStudy;
  draft?: CaseDraft;
  enabled: boolean;
  disabledMessage: string;
  onSaved: (draft: CaseDraft) => void;
  onReload: () => void;
}) {
  const responseId = useId();
  const [response, setResponse] = useState(draft?.response || "");
  const [checked, setChecked] = useState(draft?.checked_criteria || []);
  const [saved, setSaved] = useState(draft);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [conflict, setConflict] = useState(false);
  const [message, setMessage] = useState("");
  const changed =
    response !== (saved?.response || "") ||
    JSON.stringify([...checked].sort()) !==
      JSON.stringify([...(saved?.checked_criteria || [])].sort());

  async function save(event: React.FormEvent) {
    event.preventDefault();
    if (!enabled || busy || conflict) return;
    setBusy(true);
    setError("");
    setMessage("");
    try {
      const result = await api.saveCaseDraft(courseId, study.id, {
        content_version: version,
        case_sha256: study.case_sha256,
        response,
        checked_criteria: checked,
        expected_revision: saved?.revision || 0,
      });
      setSaved(result);
      onSaved(result);
      setMessage("Draft saved. Checklist marks record your own self-check.");
    } catch (error) {
      setError(errorMessage(error));
      setConflict(error instanceof ApiError && error.status === 409);
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="card case-editor" aria-label="Case response">
      <h3>Case prompt</h3>
      <p className="case-prompt">{study.prompt}</p>
      {study.limitations.map((limitation, index) => (
        <p className="notice" key={index}>
          {limitation}
        </p>
      ))}
      <form onSubmit={save}>
        <label htmlFor={responseId}>Your response</label>
        <p id={`${responseId}-help`} className="muted">
          Explain your evidence chain, controls, and remaining uncertainty.
          Saved drafts are private to your session or account. Limit: 20,000
          characters.
        </p>
        <textarea
          id={responseId}
          rows={10}
          maxLength={20000}
          aria-describedby={`${responseId}-help`}
          value={response}
          disabled={!enabled || busy}
          onChange={(event) => {
            setResponse(event.target.value);
            setMessage("");
          }}
        />
        <fieldset disabled={!enabled || busy} className="case-checklist">
          <legend>Self-check your response</legend>
          <p className="muted">
            Mark a criterion when you can identify evidence for it in your
            response. These marks do not generate a score or prove mastery.
          </p>
          {study.criteria.map((criterion) => (
            <label className="checkbox-label" key={criterion.id}>
              <input
                type="checkbox"
                checked={checked.includes(criterion.id)}
                onChange={(event) => {
                  setChecked((previous) =>
                    event.target.checked
                      ? [...previous, criterion.id]
                      : previous.filter((id) => id !== criterion.id),
                  );
                  setMessage("");
                }}
              />
              <span>{criterion.criterion}</span>
            </label>
          ))}
        </fieldset>
        {!enabled && <p className="notice">{disabledMessage}</p>}
        {enabled && (
          <div className="actions">
            <button
              className="primary"
              type="submit"
              disabled={busy || conflict || !changed}
            >
              {busy ? "Saving draft…" : "Save draft"}
            </button>
            <span className="muted">
              {changed
                ? "Unsaved changes"
                : saved
                  ? "Saved draft"
                  : "No saved draft yet"}
            </span>
          </div>
        )}
        {saved && (
          <p className="muted">
            Saved for course version {saved.content_version} · revision{" "}
            {saved.revision}.
          </p>
        )}
        {error && (
          <p role="alert" className="error">
            {error} Your editor text is retained.
          </p>
        )}
        {conflict && (
          <div className="notice">
            <p>
              Copy any unsaved text you want to keep before replacing this
              editor. If the course prompt changed, reload the course page
              first.
            </p>
            <button type="button" onClick={onReload}>
              Replace editor with saved draft
            </button>
          </div>
        )}
        <p role="status">{message}</p>
      </form>
    </section>
  );
}

export function CaseStudio({
  course,
  enrolled,
  enabled,
  archived = false,
}: {
  course: Course;
  enrolled: boolean;
  enabled: boolean;
  archived?: boolean;
}) {
  const studies = course.case_studies || [];
  const [drafts, setDrafts] = useState<CaseDraft[]>([]);
  const [loaded, setLoaded] = useState(false);
  const [error, setError] = useState("");
  const [reload, setReload] = useState(0);
  useEffect(() => {
    let active = true;
    if (!enrolled) return;
    api
      .caseDrafts(course.id)
      .then((items) => {
        if (active) {
          setDrafts(items);
          setLoaded(true);
        }
      })
      .catch((error) => {
        if (active) setError(errorMessage(error));
      });
    return () => {
      active = false;
    };
  }, [course.id, enrolled, reload]);

  function reloadDrafts() {
    setLoaded(false);
    setError("");
    setReload((previous) => previous + 1);
  }
  const availableDrafts = enrolled && loaded ? drafts : [];
  const oldDrafts = availableDrafts.filter(
    (draft) =>
      draft.content_version !== course.version ||
      !studies.some(
        (study) =>
          study.id === draft.case_id && study.case_sha256 === draft.case_sha256,
      ),
  );

  return (
    <>
      <section className="card">
        <span className="eyebrow">Ungraded written practice</span>
        <h2>Case studio</h2>
        <p>
          Write a response to an authored case, then check it against the
          supplied criteria. Your drafts and self-checks are separate from the
          practice gradebook.
        </p>
        {!studies.length && <p>No case study is authored for this package.</p>}
        {enrolled && !loaded && !error && (
          <p role="status">Loading your saved drafts…</p>
        )}
        {error && (
          <>
            <p role="alert" className="error">
              {error} Saving is disabled until your drafts can be loaded.
            </p>
            <button onClick={reloadDrafts}>Retry loading drafts</button>
          </>
        )}
      </section>
      {studies.map((study, index) => (
        <div key={study.id}>
          {studies.length > 1 && <h3>Case {index + 1}</h3>}
          {(!enrolled || loaded) && (
            <CaseEditor
              key={`${study.case_sha256}:${course.version}:${enrolled}:${reload}`}
              courseId={course.id}
              version={course.version}
              study={study}
              draft={availableDrafts.find(
                (draft) =>
                  draft.case_id === study.id &&
                  draft.content_version === course.version &&
                  draft.case_sha256 === study.case_sha256,
              )}
              enabled={enabled && loaded}
              disabledMessage={
                archived
                  ? "This archived case and its saved response are read-only."
                  : enrolled
                    ? "Update your enrollment to the current course version before saving a draft."
                    : "Start a guest session or sign in, then enroll to write and save a draft."
              }
              onSaved={(result) =>
                setDrafts((previous) => [
                  result,
                  ...previous.filter((draft) => draft.id !== result.id),
                ])
              }
              onReload={reloadDrafts}
            />
          )}
        </div>
      ))}
      {oldDrafts.length > 0 && (
        <section className="card" aria-label="Earlier case drafts">
          <h3>Earlier case drafts</h3>
          <p>
            Responses to earlier versions or changed prompts remain available
            here and in your account export.
          </p>
          {oldDrafts.map((draft) => (
            <details key={draft.id}>
              <summary>
                Version {draft.content_version} · saved{" "}
                {new Date(draft.updated_at).toLocaleString()}
              </summary>
              <h4>Saved prompt</h4>
              <p>{draft.case_snapshot.prompt}</p>
              <h4>Saved response</h4>
              <p className="case-saved-response">
                {draft.response || "Empty response"}
              </p>
              <h4>Your saved self-checks</h4>
              <ul>
                {draft.case_snapshot.criteria.map((criterion) => (
                  <li key={criterion.id}>
                    {draft.checked_criteria.includes(criterion.id)
                      ? "Marked: "
                      : "Unmarked: "}
                    {criterion.criterion}
                  </li>
                ))}
              </ul>
            </details>
          ))}
        </section>
      )}
    </>
  );
}

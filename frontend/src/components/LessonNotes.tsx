import { useEffect, useRef, useState } from "react";
import { errorMessage } from "../api";
import type { Note } from "../types";

export function LessonNotes({
  note,
  enabled,
  disabledMessage,
  onSave,
}: {
  note?: Note;
  enabled: boolean;
  disabledMessage?: string;
  onSave: (body: string) => Promise<void>;
}) {
  const [draft, setDraft] = useState({
    body: note?.body || "",
    savedBody: note?.body || "",
  });
  const [busy, setBusy] = useState(false);
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState("");
  const saving = useRef(false);
  const changed = draft.body !== draft.savedBody;

  useEffect(() => {
    const savedBody = note?.body || "";
    const wasSaving = saving.current;
    setDraft((previous) => ({
      // A delayed load or save acknowledgement must not replace newer typing.
      body:
        !wasSaving && previous.body === previous.savedBody
          ? savedBody
          : previous.body,
      savedBody,
    }));
  }, [note?.body]);

  async function save() {
    if (!enabled || saving.current) return;
    const submittedBody = draft.body;
    saving.current = true;
    setBusy(true);
    setSaved(false);
    setError("");
    try {
      await onSave(submittedBody);
      setDraft((previous) => ({ ...previous, savedBody: submittedBody }));
      setSaved(true);
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      saving.current = false;
      setBusy(false);
    }
  }

  return (
    <section className="card">
      <h2>Lesson notes</h2>
      <label>
        Your private note
        <textarea
          value={draft.body}
          onChange={(event) => {
            const body = event.target.value;
            setDraft((previous) => ({ ...previous, body }));
            setSaved(false);
          }}
          maxLength={20000}
          rows={6}
          disabled={!enabled}
        />
      </label>
      <button onClick={save} disabled={!enabled || busy || !changed}>
        {busy ? "Saving…" : "Save note"}
      </button>
      {!enabled && (
        <p className="muted">
          {disabledMessage ||
            "Enroll to save notes to your account or guest session."}
        </p>
      )}
      <p role="status">
        {busy
          ? "Saving note…"
          : changed
            ? "Unsaved changes."
            : saved
              ? "Note saved."
              : ""}
      </p>
      {error && (
        <p role="alert" className="error">
          {error}
        </p>
      )}
    </section>
  );
}

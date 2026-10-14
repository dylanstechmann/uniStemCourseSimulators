import { useEffect, useState } from "react";
import { api, errorMessage } from "../api";
import type { CourseSummary, NotebookNote, NotebookPage } from "../types";

const pageSize = 50;

export function NotebookView({
  hasSession,
  courses,
  needsVersionReview,
}: {
  hasSession: boolean;
  courses: CourseSummary[];
  needsVersionReview: boolean;
}) {
  const [query, setQuery] = useState("");
  const [courseId, setCourseId] = useState("");
  const [offset, setOffset] = useState(0);
  const [page, setPage] = useState<NotebookPage | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);

  useEffect(() => {
    let active = true;
    if (!hasSession) {
      setPage(null);
      setLoading(false);
      return () => {
        active = false;
      };
    }

    setLoading(true);
    setError("");
    const timer = window.setTimeout(() => {
      api
        .notebook(query, courseId || undefined, offset)
        .then((result) => {
          if (active) setPage(result);
        })
        .catch((requestError) => {
          if (active) setError(errorMessage(requestError));
        })
        .finally(() => {
          if (active) setLoading(false);
        });
    }, 200);

    return () => {
      active = false;
      window.clearTimeout(timer);
    };
  }, [hasSession, query, courseId, offset, refreshKey]);

  function updateQuery(value: string) {
    setQuery(value);
    setOffset(0);
  }

  function updateCourse(value: string) {
    setCourseId(value);
    setOffset(0);
  }

  const items: NotebookNote[] = page?.items ?? [];
  const total = page?.total ?? 0;

  return (
    <>
      <span className="eyebrow">Your private study notes</span>
      <h1>My notes</h1>
      {!hasSession ? (
        <p className="notice">
          <a href="#/account">Start a guest session or sign in</a> to search
          your saved lesson notes.
        </p>
      ) : (
        <>
          <p className="lead notebook-intro">
            Search notes saved in your enrolled courses. Search checks note
            text; use the course filter to narrow the results. Notes stay
            private to your session.
          </p>
          {needsVersionReview ? (
            <p className="notice">
              Notes in courses that need an enrollment version review are
              temporarily hidden. Open that course from My learning to review
              the update.
            </p>
          ) : null}
          <section className="card notebook-search" aria-label="Search notes">
            <label htmlFor="notebook-query">Search saved note text</label>
            <input
              id="notebook-query"
              type="search"
              value={query}
              onChange={(event) => updateQuery(event.currentTarget.value)}
              maxLength={200}
              placeholder="Try a term, equation, or question"
            />
            <label htmlFor="notebook-course">Course</label>
            <select
              id="notebook-course"
              value={courseId}
              onChange={(event) => updateCourse(event.currentTarget.value)}
            >
              <option value="">All current courses</option>
              {courses.map((course) => (
                <option key={course.id} value={course.id}>
                  {course.title}
                </option>
              ))}
            </select>
          </section>
          {loading ? <p role="status">Searching notes…</p> : null}
          {error ? (
            <div className="error" role="alert">
              <p>{error}</p>
              <button onClick={() => setRefreshKey((value) => value + 1)}>
                Try again
              </button>
            </div>
          ) : null}
          {!loading && !error ? (
            <>
              <p className="notebook-result-count" aria-live="polite">
                {query.trim()
                  ? `${total} matching ${total === 1 ? "note" : "notes"}`
                  : `${total} saved ${total === 1 ? "note" : "notes"}`}
              </p>
              {items.length ? (
                <div className="notebook-results">
                  {items.map((note) => (
                    <article
                      className="card notebook-entry"
                      key={`${note.course_id}:${note.lesson_id}`}
                    >
                      <div className="section-heading">
                        <div>
                          <span className="eyebrow">{note.course_title}</span>
                          <h2>
                            <a
                              href={`#/course/${encodeURIComponent(note.course_id)}/lesson/${encodeURIComponent(note.lesson_id)}`}
                            >
                              {note.lesson_title}
                            </a>
                          </h2>
                        </div>
                        <time dateTime={note.updated_at}>
                          Saved {new Date(note.updated_at).toLocaleString()}
                        </time>
                      </div>
                      <p className="notebook-body">{note.body}</p>
                    </article>
                  ))}
                </div>
              ) : total === 0 ? (
                <p className="notice">
                  {query.trim()
                    ? "No notes match that search. Try another term or clear the course filter."
                    : courses.length
                      ? "No saved lesson notes yet. Open a lesson in My learning and add a private note."
                      : "Enroll in a course to start saving lesson notes."}
                </p>
              ) : null}
              {total > pageSize ? (
                <nav className="notebook-pagination" aria-label="Note results">
                  <button
                    onClick={() => setOffset(Math.max(0, offset - pageSize))}
                    disabled={offset === 0}
                  >
                    Previous notes
                  </button>
                  <span>
                    {offset + 1}–{Math.min(offset + items.length, total)} of{" "}
                    {total}
                  </span>
                  <button
                    onClick={() => setOffset(offset + pageSize)}
                    disabled={offset + pageSize >= total}
                  >
                    More notes
                  </button>
                </nav>
              ) : null}
            </>
          ) : null}
        </>
      )}
    </>
  );
}

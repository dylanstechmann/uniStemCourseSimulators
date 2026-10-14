import { useEffect, useState } from "react";
import { api, errorMessage } from "../api";
import type {
  Attempt,
  AssessmentPlan,
  CardRating,
  Course,
  CourseSummary,
  Gradebook,
  GradedSubmission,
  Lesson,
  Note,
  Progress,
  ReviewQueue,
  Source,
} from "../types";
import { GradebookView } from "./GradebookView";
import { AssessmentPlanView } from "./AssessmentPlanView";
import { LessonStudy } from "./LessonStudy";
import { MarkdownReader } from "./MarkdownReader";
import { MaturityBadge } from "./MaturityBadge";
import { GradedAssessment } from "./GradedAssessment";
import { PracticeAssessmentView } from "./PracticeAssessmentView";
import { ReviewQueueView } from "./ReviewQueueView";
import { CourseSchedule } from "./CourseSchedule";
import { CaseStudio } from "./CaseStudio";

export function CourseWorkspace({
  id,
  archivedVersion,
  lessonId,
  assessmentId,
  showGradebook,
  showReview = false,
  showCases = false,
  enrollmentVersion,
  catalog,
  enrolled,
  hasSession,
  bookmarked,
  sources,
  onEnroll,
  onUpgrade,
  onBookmark,
}: {
  id: string;
  archivedVersion?: string;
  lessonId?: string;
  assessmentId?: string;
  showGradebook: boolean;
  showReview?: boolean;
  showCases?: boolean;
  enrollmentVersion?: string;
  catalog: CourseSummary[];
  enrolled: boolean;
  hasSession: boolean;
  bookmarked: boolean;
  sources: Source[];
  onEnroll: () => Promise<void>;
  onUpgrade: () => Promise<void>;
  onBookmark: (saved: boolean) => Promise<void>;
}) {
  const [course, setCourse] = useState<Course | null>(null);
  const [archivedVersions, setArchivedVersions] = useState<string[]>([]);
  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [progress, setProgress] = useState<Progress[]>([]);
  const [notes, setNotes] = useState<Note[]>([]);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [gradebook, setGradebook] = useState<Gradebook | null>(null);
  const [assessmentPlan, setAssessmentPlan] = useState<AssessmentPlan | null>(
    null,
  );
  const [gradedSubmissions, setGradedSubmissions] = useState<
    GradedSubmission[]
  >([]);
  const [activeGradedAssessmentId, setActiveGradedAssessmentId] = useState<
    string | null
  >(null);
  const [activePracticeAssessmentId, setActivePracticeAssessmentId] = useState<
    string | null
  >(null);
  const [reviewQueue, setReviewQueue] = useState<ReviewQueue | null>(null);
  const [reviewError, setReviewError] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    let active = true;
    setCourse(null);
    setError("");
    setActiveGradedAssessmentId(null);
    setActivePracticeAssessmentId(null);
    (archivedVersion ? api.archivedCourse(id, archivedVersion) : api.course(id))
      .then((data) => {
        if (active) setCourse(data);
      })
      .catch((error) => {
        if (active) setError(errorMessage(error));
      });
    return () => {
      active = false;
    };
  }, [id, archivedVersion]);
  useEffect(() => {
    let active = true;
    if (!enrolled || archivedVersion) {
      setArchivedVersions([]);
      return;
    }
    api
      .archivedCourseVersions(id)
      .then((versions) => {
        if (active) setArchivedVersions(versions);
      })
      .catch(() => {
        if (active) setArchivedVersions([]);
      });
    return () => {
      active = false;
    };
  }, [id, enrolled, archivedVersion]);
  useEffect(() => {
    let active = true;
    setLesson(null);
    if (lessonId)
      (archivedVersion
        ? api.archivedLesson(id, archivedVersion, lessonId)
        : api.lesson(id, lessonId)
      )
        .then((data) => {
          if (active) setLesson(data);
        })
        .catch((error) => {
          if (active) setError(errorMessage(error));
        });
    return () => {
      active = false;
    };
  }, [id, archivedVersion, lessonId]);
  useEffect(() => {
    let active = true;
    if (
      archivedVersion ||
      !enrolled ||
      !course ||
      (enrollmentVersion && enrollmentVersion !== course.version)
    ) {
      setProgress([]);
      setNotes([]);
      setAttempts([]);
      setGradebook(null);
      setAssessmentPlan(null);
      setGradedSubmissions([]);
      setReviewQueue(null);
      return;
    }
    setReviewError("");
    api
      .reviewQueue(id)
      .then((queue) => {
        if (active) setReviewQueue(queue);
      })
      .catch((error) => {
        if (active) setReviewError(errorMessage(error));
      });
    Promise.all([
      api.progress(id),
      api.notes(id),
      api.attempts(id),
      api.gradebook(id),
      api.assessmentPlan(id),
      api.gradedSubmissions(id),
    ])
      .then(
        ([
          progress,
          notes,
          attempts,
          gradebook,
          assessmentPlan,
          gradedSubmissions,
        ]) => {
          if (active) {
            setProgress(progress);
            setNotes(notes);
            setAttempts(attempts);
            setGradebook(gradebook);
            setAssessmentPlan(assessmentPlan);
            setGradedSubmissions(gradedSubmissions);
          }
        },
      )
      .catch((error) => {
        if (active) setError(errorMessage(error));
      });
    return () => {
      active = false;
    };
  }, [id, archivedVersion, enrolled, course, enrollmentVersion]);
  useEffect(() => {
    if (!showGradebook || !assessmentId) {
      setActiveGradedAssessmentId(null);
      setActivePracticeAssessmentId(null);
      return;
    }
    if (!assessmentPlan) return;
    const selected = assessmentPlan.assessments.find(
      (assessment) => assessment.id === assessmentId,
    );
    setActiveGradedAssessmentId(
      selected?.mode === "graded" ? selected.id : null,
    );
    setActivePracticeAssessmentId(
      selected?.mode === "practice" ? selected.id : null,
    );
  }, [assessmentId, assessmentPlan, showGradebook]);
  async function enroll() {
    setBusy(true);
    setError("");
    try {
      await onEnroll();
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function bookmark() {
    setBusy(true);
    setError("");
    try {
      await onBookmark(!bookmarked);
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function upgrade() {
    setBusy(true);
    setError("");
    try {
      await onUpgrade();
    } catch (error) {
      setError(errorMessage(error));
    } finally {
      setBusy(false);
    }
  }
  async function submit(
    question: string,
    response: string | number | number[] | Record<string, string>,
    unit?: string,
    variantToken?: string | null,
  ) {
    const attempt = await api.attempt(
      id,
      question,
      response,
      unit,
      variantToken,
    );
    setAttempts((previous) => [...previous, attempt]);
    setGradebook(await api.gradebook(id));
    return attempt;
  }
  async function requestAppeal(attemptId: string, reason: string) {
    const appeal = await api.requestAppeal(attemptId, reason);
    setAttempts((previous) =>
      previous.map((attempt) =>
        attempt.id === attemptId
          ? { ...attempt, appeal, effective_score: appeal.effective_score }
          : attempt,
      ),
    );
    setGradebook(await api.gradebook(id));
    return appeal;
  }
  async function refreshAfterGradedSubmission(submission: GradedSubmission) {
    setGradedSubmissions((previous) => [...previous, submission]);
    const [nextGradebook, nextPlan, nextSubmissions] = await Promise.all([
      api.gradebook(id),
      api.assessmentPlan(id),
      api.gradedSubmissions(id),
    ]);
    setGradebook(nextGradebook);
    setAssessmentPlan(nextPlan);
    setGradedSubmissions(nextSubmissions);
  }
  async function requestGradedAppeal(submissionId: string, reason: string) {
    const appeal = await api.requestGradedAppeal(submissionId, reason);
    setGradedSubmissions((previous) =>
      previous.map((submission) =>
        submission.id === submissionId
          ? {
              ...submission,
              appeal,
              effective_score: appeal.effective_score,
              effective_score_percent:
                Math.round(
                  (appeal.effective_score / submission.max_score) * 10000,
                ) / 100,
            }
          : submission,
      ),
    );
    return appeal;
  }
  async function rateCard(cardId: string, rating: CardRating) {
    const result = await api.reviewCard(id, cardId, rating);
    try {
      setReviewQueue(await api.reviewQueue(id));
      setReviewError("");
    } catch (error) {
      setReviewError(errorMessage(error));
    }
    return result;
  }
  const cardSchedules = Object.fromEntries(
    reviewQueue
      ? [...reviewQueue.due, ...reviewQueue.new, ...reviewQueue.upcoming].map(
          (card) => [card.card_id, card.schedule],
        )
      : [],
  );
  async function saveNote(body: string) {
    const note = await api.saveNote(id, lessonId!, body);
    setNotes((previous) => [
      ...previous.filter((item) => item.lesson_id !== lessonId),
      note,
    ]);
  }
  async function markProgress(completed: boolean) {
    const mark = await api.setProgress(id, lessonId!, completed);
    setProgress((previous) => [
      ...previous.filter((item) => item.lesson_id !== lessonId),
      mark,
    ]);
  }
  const courseLink = archivedVersion
    ? `#/course/${encodeURIComponent(id)}/version/${encodeURIComponent(archivedVersion)}`
    : `#/course/${encodeURIComponent(id)}`;
  function prerequisites(ids: string[]) {
    return ids.length ? (
      <ul>
        {ids.map((prerequisite) => (
          <li key={prerequisite}>
            <a href={`#/course/${encodeURIComponent(prerequisite)}`}>
              {catalog.find((item) => item.id === prerequisite)?.title ||
                prerequisite}
            </a>
          </li>
        ))}
      </ul>
    ) : (
      <p>None represented in the current course graph.</p>
    );
  }
  if (!course)
    return (
      <>
        <h1>Course workspace</h1>
        {error ? (
          <p className="error" role="alert">
            {error}
          </p>
        ) : (
          <p role="status">Loading course…</p>
        )}
      </>
    );
  const needsVersionReview = Boolean(
    !archivedVersion &&
    enrolled &&
    enrollmentVersion &&
    enrollmentVersion !== course.version,
  );
  return (
    <>
      <div className="section-heading">
        <div>
          <span className="eyebrow">
            {course.domain} · {course.level}
          </span>
          <h1>{course.title}</h1>
          <div className="inline-meta">
            <MaturityBadge maturity={course.maturity} />
            <span>Content v{course.version}</span>
            <span>{course.lesson_count} available lessons</span>
          </div>
        </div>
        {!archivedVersion && (
          <div className="actions">
            {!enrolled && (
              <button
                className="primary"
                onClick={enroll}
                disabled={!hasSession || busy}
              >
                Enroll in partial course
              </button>
            )}
            {enrolled && <span className="tag">Enrolled</span>}
            <button
              onClick={bookmark}
              disabled={!hasSession || busy}
              aria-pressed={bookmarked}
            >
              {bookmarked ? "Remove bookmark" : "Bookmark course"}
            </button>
          </div>
        )}
      </div>
      <p className="lead">{course.description}</p>
      {!archivedVersion &&
        archivedVersions.some((version) => version !== course.version) && (
          <section className="card" aria-labelledby="archived-versions-title">
            <h2 id="archived-versions-title">Earlier archived versions</h2>
            <p className="muted">
              These saved public packages open in read-only mode.
            </p>
            <ul>
              {archivedVersions
                .filter((version) => version !== course.version)
                .map((version) => (
                  <li key={version}>
                    <a
                      href={`#/course/${encodeURIComponent(id)}/version/${encodeURIComponent(version)}`}
                    >
                      Read version {version}
                    </a>
                  </li>
                ))}
            </ul>
          </section>
        )}
      {archivedVersion && (
        <aside className="notice" aria-label="Archived course version">
          <strong>Archived package · read-only</strong>
          <p>
            You are viewing the saved public content for version{" "}
            {archivedVersion}. Practice, notes, progress marks, and card ratings
            are disabled here.
          </p>
          <a href={`#/course/${encodeURIComponent(id)}`}>
            Open the current course version (
            {catalog.find((item) => item.id === id)?.version || "current"})
          </a>
          {!!course.case_studies?.length && (
            <p>
              <a href={`${courseLink}/cases`}>Read archived case studio</a>
            </p>
          )}
        </aside>
      )}
      {needsVersionReview && (
        <aside className="notice" aria-label="Course content update">
          <strong>Course content updated</strong>
          <p>
            Your saved attempts and reading marks remain attached to version{" "}
            {enrollmentVersion}. Review the current partial package and update
            your enrollment to continue saving work.
          </p>
          <p>
            <a
              href={`#/course/${encodeURIComponent(id)}/version/${encodeURIComponent(enrollmentVersion || "")}`}
            >
              Read your enrolled version ({enrollmentVersion})
            </a>
          </p>
          <button
            className="primary"
            onClick={upgrade}
            disabled={!hasSession || busy}
          >
            Update enrollment to version {course.version}
          </button>
        </aside>
      )}
      {!hasSession && (
        <p className="notice">
          <a href="#/account">Start a guest session or sign in</a> to enroll and
          save work. Public lesson reading remains available.
        </p>
      )}
      {course.limitations.length > 0 && (
        <aside className="notice" aria-label="Course limitations">
          <strong>Current limitations</strong>
          <p>{course.limitations[0]}</p>
          {course.limitations.length > 1 && (
            <details>
              <summary>
                Read all {course.limitations.length} course limitations
              </summary>
              <ul>
                {course.limitations.map((limitation, index) => (
                  <li key={index}>{limitation}</li>
                ))}
              </ul>
            </details>
          )}
        </aside>
      )}
      {error && (
        <p role="alert" className="error">
          {error}
        </p>
      )}
      {!archivedVersion && (
        <nav className="tabs" aria-label="Course views">
          <a
            href={courseLink}
            aria-current={
              !lessonId && !showGradebook && !showReview && !showCases
                ? "page"
                : undefined
            }
          >
            Syllabus and lessons
          </a>
          <a
            href={`${courseLink}/gradebook`}
            aria-current={showGradebook ? "page" : undefined}
          >
            Practice gradebook
          </a>
          <a
            href={`${courseLink}/review`}
            aria-current={showReview ? "page" : undefined}
          >
            Review queue
            {reviewQueue && reviewQueue.counts.due > 0
              ? ` (${reviewQueue.counts.due} due)`
              : ""}
          </a>
          <a href="#/tools">Study tools</a>
          {!!course.case_studies?.length && (
            <a
              href={`${courseLink}/cases`}
              aria-current={showCases ? "page" : undefined}
            >
              Case studio
            </a>
          )}
        </nav>
      )}
      <div className={`workspace-grid${showCases ? " case-workspace" : ""}`}>
        {!showCases && (
          <aside className="card lesson-navigation">
            <h2>Available lessons</h2>
            {!archivedVersion && (
              <p className="muted">
                {progress.filter((item) => item.completed).length} marked read.
                This is self-reported progress.
              </p>
            )}
            <nav aria-label="Lessons">
              {course.modules.map((module) => (
                <section key={module.id}>
                  <h3>{module.title}</h3>
                  <ol>
                    {module.lessons.map((item) => (
                      <li key={item.id}>
                        <a
                          href={`${courseLink}/lesson/${encodeURIComponent(item.id)}`}
                          aria-current={
                            lessonId === item.id ? "page" : undefined
                          }
                        >
                          {item.title}
                        </a>
                        {!archivedVersion &&
                          progress.some(
                            (mark) =>
                              mark.lesson_id === item.id && mark.completed,
                          ) && <span className="read-label">Read</span>}
                      </li>
                    ))}
                  </ol>
                </section>
              ))}
            </nav>
          </aside>
        )}
        <div className="workspace-main">
          {showCases ? (
            <CaseStudio
              key={`${course.version}:${enrolled}`}
              course={course}
              enrolled={enrolled && hasSession}
              enabled={
                enrolled &&
                hasSession &&
                !needsVersionReview &&
                !archivedVersion
              }
              archived={!!archivedVersion}
            />
          ) : archivedVersion ? (
            lessonId ? (
              lesson ? (
                <LessonStudy
                  key={`${archivedVersion}:${lesson.id}`}
                  lesson={lesson}
                  enabled={false}
                  disabledMessage={`Version ${archivedVersion} is archived and read-only.`}
                  completed={false}
                  attempts={[]}
                  sources={sources}
                  onAttempt={async () => {
                    throw new Error("Archived lessons are read-only.");
                  }}
                  onAppeal={async () => {
                    throw new Error("Archived lessons are read-only.");
                  }}
                  onSaveNote={async () => {
                    throw new Error("Archived lessons are read-only.");
                  }}
                  onProgress={async () => {
                    throw new Error("Archived lessons are read-only.");
                  }}
                />
              ) : (
                <p role="status">Loading archived lesson…</p>
              )
            ) : (
              <>
                <CourseSchedule
                  courseId={id}
                  weeks={course.weeks}
                  linkPrefix={courseLink}
                  readOnly
                />
                <section className="card">
                  <h2>Syllabus</h2>
                  <MarkdownReader>{course.syllabus_markdown}</MarkdownReader>
                  <h3>Prerequisite knowledge</h3>
                  <p>{course.prerequisites.statement}</p>
                  <ul>
                    {course.prerequisites.knowledge.map((knowledge, index) => (
                      <li key={index}>{knowledge}</li>
                    ))}
                  </ul>
                </section>
                <section className="card">
                  <h2>Learning outcomes</h2>
                  <ul className="objectives">
                    {course.outcomes.map((objective) => (
                      <li key={objective.id}>
                        <span className="tag">{objective.bloom}</span>{" "}
                        {objective.description}
                      </li>
                    ))}
                  </ul>
                  <p className="muted">Content license: {course.license}.</p>
                </section>
              </>
            )
          ) : showGradebook ? (
            enrolled && !needsVersionReview && gradebook ? (
              <>
                {assessmentPlan && (
                  <AssessmentPlanView
                    plan={assessmentPlan}
                    onOpenAssessment={(assessmentId) => {
                      setActivePracticeAssessmentId(null);
                      setActiveGradedAssessmentId(assessmentId);
                    }}
                    onOpenPractice={(assessmentId) => {
                      setActiveGradedAssessmentId(null);
                      setActivePracticeAssessmentId(assessmentId);
                    }}
                  />
                )}
                {activeGradedAssessmentId && (
                  <GradedAssessment
                    key={activeGradedAssessmentId}
                    courseId={id}
                    assessmentId={activeGradedAssessmentId}
                    enabled={enrolled && !needsVersionReview}
                    history={gradedSubmissions}
                    onSubmitted={refreshAfterGradedSubmission}
                    onAppeal={requestGradedAppeal}
                  />
                )}
                {activePracticeAssessmentId && (
                  <PracticeAssessmentView
                    key={activePracticeAssessmentId}
                    courseId={id}
                    assessmentId={activePracticeAssessmentId}
                    enabled={enrolled && !needsVersionReview}
                    attempts={attempts}
                    onSubmit={submit}
                    onAppeal={requestAppeal}
                    onClose={() => {
                      setActivePracticeAssessmentId(null);
                      if (assessmentId) {
                        window.location.hash = `${courseLink}/gradebook`;
                      }
                    }}
                  />
                )}
                <GradebookView
                  gradebook={gradebook}
                  attempts={attempts}
                  course={course}
                />
              </>
            ) : (
              <section className="card">
                <h2>Practice gradebook</h2>
                <p>
                  {needsVersionReview
                    ? "Update your enrollment to access current practice tools. Prior attempts and feedback remain available after the update."
                    : enrolled
                      ? "Loading saved practice evidence…"
                      : "Enroll to view your practice attempts and gradebook."}
                </p>
              </section>
            )
          ) : showReview ? (
            enrolled && !needsVersionReview && reviewQueue ? (
              <ReviewQueueView
                courseId={id}
                queue={reviewQueue}
                enabled={enrolled && !needsVersionReview}
                onRate={rateCard}
              />
            ) : (
              <section className="card">
                <h2>Spaced retrieval review</h2>
                {reviewError ? (
                  <p role="alert" className="error">
                    {reviewError}
                  </p>
                ) : (
                  <p>
                    {needsVersionReview
                      ? "Update your enrollment to review this package's current retrieval cards."
                      : enrolled
                        ? "Loading your review schedule…"
                        : "Enroll to schedule retrieval-card reviews. Card text remains readable in each lesson."}
                  </p>
                )}
              </section>
            )
          ) : lessonId ? (
            lesson ? (
              <LessonStudy
                key={lesson.id}
                lesson={lesson}
                enabled={enrolled && !needsVersionReview}
                disabledMessage={
                  needsVersionReview
                    ? "Update your enrollment before saving new attempts or reading progress."
                    : undefined
                }
                note={notes.find((item) => item.lesson_id === lessonId)}
                completed={progress.some(
                  (item) => item.lesson_id === lessonId && item.completed,
                )}
                attempts={attempts}
                sources={sources}
                onAttempt={submit}
                onAppeal={requestAppeal}
                onSaveNote={saveNote}
                onProgress={markProgress}
                cardSchedules={cardSchedules}
                onRateCard={
                  enrolled && !needsVersionReview ? rateCard : undefined
                }
              />
            ) : (
              <p role="status">Loading lesson…</p>
            )
          ) : (
            <>
              <CourseSchedule courseId={id} weeks={course.weeks} />
              <section className="card">
                <h2>Syllabus</h2>
                <MarkdownReader>{course.syllabus_markdown}</MarkdownReader>
                <h3>Prerequisite knowledge</h3>
                <p>{course.prerequisites.statement}</p>
                <ul>
                  {course.prerequisites.knowledge.map((knowledge, index) => (
                    <li key={index}>{knowledge}</li>
                  ))}
                </ul>
                <h3>Required course dependencies</h3>
                {prerequisites(course.prerequisites.course_ids)}
                <h3>Recommended preparation</h3>
                {prerequisites(course.prerequisites.recommended_course_ids)}
                <h3>Concurrent course dependencies</h3>
                {prerequisites(course.prerequisites.concurrent_course_ids)}
                <p className="muted">
                  These are uniStemCourseSimulators learning dependencies. They
                  do not establish university prerequisite equivalency.
                </p>
              </section>
              <section className="card">
                <h2>Learning outcomes</h2>
                <ul className="objectives">
                  {course.outcomes.map((objective) => (
                    <li key={objective.id}>
                      <span className="tag">{objective.bloom}</span>{" "}
                      {objective.description}
                    </li>
                  ))}
                </ul>
                <p className="muted">
                  Content license: {course.license}. Completion and external
                  review are not claimed for this partial package.
                </p>
              </section>
            </>
          )}
        </div>
      </div>
    </>
  );
}

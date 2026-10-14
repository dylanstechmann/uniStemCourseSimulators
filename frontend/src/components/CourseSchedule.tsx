import type { CourseWeek } from "../types";

export function CourseSchedule({
  courseId,
  weeks,
  linkPrefix,
  readOnly = false,
}: {
  courseId: string;
  weeks: CourseWeek[];
  linkPrefix?: string;
  readOnly?: boolean;
}) {
  if (!weeks.length) return null;
  const courseLink = linkPrefix || `#/course/${encodeURIComponent(courseId)}`;

  return (
    <section
      className="card course-schedule"
      aria-labelledby="course-schedule-title"
    >
      <div className="section-heading">
        <div>
          <h2 id="course-schedule-title">Course schedule</h2>
          <p className="muted">
            Authored week sequence. Week numbers are not calendar dates, and
            learner workload has not been measured.
          </p>
        </div>
        <span className="tag">{weeks.length} weeks</span>
      </div>
      <ol className="course-week-list">
        {weeks.map((week) => (
          <li className="course-week" key={week.week}>
            <div className="course-week-content">
              <h3 aria-label={`Week ${week.week}: ${week.title}`}>
                <span className="course-week-number">Week {week.week}:</span>{" "}
                {week.title}
              </h3>
              <h4>Lessons</h4>
              {week.lessons.length ? (
                <ul>
                  {week.lessons.map((lesson) => (
                    <li key={lesson.id}>
                      <a
                        href={`${courseLink}/lesson/${encodeURIComponent(lesson.id)}`}
                      >
                        {lesson.title}
                      </a>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="muted">No lesson is scheduled this week.</p>
              )}
              <h4>Activities</h4>
              {week.assessments.length ? (
                <ul>
                  {week.assessments.map((assessment) => (
                    <li key={assessment.id}>
                      <span className="tag">{assessment.type}</span>{" "}
                      {assessment.type === "case" &&
                      assessment.mode === "self-assessment" ? (
                        <a href={`${courseLink}/cases`}>{assessment.title}</a>
                      ) : !readOnly &&
                        (assessment.mode === "practice" ||
                          assessment.mode === "graded") ? (
                        <a
                          href={`${courseLink}/gradebook/assessment/${encodeURIComponent(assessment.id)}`}
                        >
                          {assessment.title}
                        </a>
                      ) : (
                        assessment.title
                      )}{" "}
                      · {assessment.mode.replaceAll("-", " ")}
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="muted">No activity is listed this week.</p>
              )}
            </div>
          </li>
        ))}
      </ol>
    </section>
  );
}

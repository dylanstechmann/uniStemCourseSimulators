import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { api } from "../api";
import type {
  AssessmentPlan,
  Course,
  Gradebook,
  Lesson,
  ReviewQueue,
} from "../types";
import { CourseWorkspace } from "./CourseWorkspace";

const course: Course = {
  id: "cell-biology",
  title: "Foundations of Cell and Molecular Biology",
  description: "A partial course fixture.",
  domain: "Life sciences",
  level: "Year 1",
  maturity: "partial",
  version: "0.35.0",
  lesson_count: 1,
  limitations: ["This package remains formative-only."],
  prerequisites: {
    course_ids: [],
    recommended_course_ids: [],
    concurrent_course_ids: [],
    knowledge: [],
    statement: "No prerequisites are required for this fixture.",
  },
  outcomes: [],
  lesson_objectives: [],
  modules: [],
  weeks: [],
  syllabus_markdown: "A test syllabus.",
  license: "CC-BY-4.0",
  review_status: "unreviewed",
  assessment_policy: {},
};

const assessmentPlan: AssessmentPlan = {
  course_id: course.id,
  content_version: course.version,
  grading_mode: "formative-only",
  course_grade_status: "not_configured",
  categories: [],
  category_aggregation: "points",
  attempt_policy: "Unlimited practice.",
  solution_release: "After submission.",
  late_policy: "No deadlines.",
  appeals: "Request a human review.",
  assessments: [
    {
      id: "practice-one",
      title: "Control-selection practice",
      type: "practice",
      mode: "practice",
      category_id: null,
      week: 1,
      points: 1,
      item_count: 1,
      objective_count: 1,
      release_at: null,
      due_at: null,
      attempt_limit: null,
      attempt_scoring: "highest",
      schedule_status: "practice",
    },
  ],
};

const gradebook: Gradebook = {
  course_id: course.id,
  assessment_role: "formative",
  aggregation: "best result per question",
  score: 0,
  max_score: 0,
  attempt_count: 0,
  manual_override_count: 0,
  objective_evidence_policy: {
    version: "practice-evidence-v1",
    minimum_distinct_items: 3,
    minimum_item_coverage: 0.8,
    minimum_performance: 0.8,
  },
  objective_evidence: {},
  limitations: "Formative practice does not establish course completion.",
};

const reviewQueue: ReviewQueue = {
  course_id: course.id,
  content_version: course.version,
  policy_version: "retrieval-schedule-v1",
  policy: "Self-rated retrieval practice.",
  generated_at: "2026-10-10T12:00:00Z",
  counts: { due: 0, new: 0, upcoming: 0 },
  due: [],
  new: [],
  upcoming: [],
  limitations: "Self-ratings are not grades.",
};

describe("course schedule activity deep links", () => {
  it("opens the matching practice activity from the enrollment-pinned plan", async () => {
    vi.spyOn(api, "course").mockResolvedValue(course);
    vi.spyOn(api, "reviewQueue").mockResolvedValue(reviewQueue);
    vi.spyOn(api, "progress").mockResolvedValue([]);
    vi.spyOn(api, "notes").mockResolvedValue([]);
    vi.spyOn(api, "attempts").mockResolvedValue([]);
    vi.spyOn(api, "gradebook").mockResolvedValue(gradebook);
    vi.spyOn(api, "assessmentPlan").mockResolvedValue(assessmentPlan);
    vi.spyOn(api, "gradedSubmissions").mockResolvedValue([]);
    vi.spyOn(api, "practiceAssessment").mockResolvedValue({
      course_id: course.id,
      assessment_id: "practice-one",
      title: "Control-selection practice",
      content_version: course.version,
      points: 1,
      questions: [],
    });
    vi.spyOn(api, "archivedCourseVersions").mockResolvedValue([
      "0.34.0",
      course.version,
    ]);

    render(
      <CourseWorkspace
        id={course.id}
        assessmentId="practice-one"
        showGradebook
        enrollmentVersion={course.version}
        catalog={[course]}
        enrolled
        hasSession
        bookmarked={false}
        sources={[]}
        onEnroll={async () => {}}
        onUpgrade={async () => {}}
        onBookmark={async () => {}}
      />,
    );

    expect(
      await screen.findByRole("heading", {
        name: "Control-selection practice",
      }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "Read version 0.34.0" }),
    ).toHaveAttribute("href", "#/course/cell-biology/version/0.34.0");
  });

  it("renders an archived package read-only and links within its saved version", async () => {
    const archivedCourse: Course = {
      ...course,
      version: "0.34.0",
      modules: [
        {
          id: "module-one",
          title: "Controls",
          source_ids: [],
          lessons: [
            {
              id: "lesson-one",
              title: "Archived lesson",
              learning_objective_ids: [],
            },
          ],
        },
      ],
      weeks: [
        {
          week: 1,
          title: "Archived week",
          lessons: [{ id: "lesson-one", title: "Archived lesson" }],
          assessments: [],
        },
      ],
    };
    const archivedLesson: Lesson = {
      id: "lesson-one",
      title: "Archived lesson",
      markdown: "This is the saved reading.",
      learning_objective_ids: [],
      source_ids: [],
      worked_example: "",
      questions: [],
      retrieval_cards: [],
    };
    const archivedCourseRequest = vi
      .spyOn(api, "archivedCourse")
      .mockResolvedValue(archivedCourse);
    const archivedLessonRequest = vi
      .spyOn(api, "archivedLesson")
      .mockResolvedValue(archivedLesson);
    const currentCourseRequest = vi.spyOn(api, "course");
    const progressRequest = vi.spyOn(api, "progress");

    render(
      <CourseWorkspace
        id={course.id}
        archivedVersion="0.34.0"
        lessonId="lesson-one"
        showGradebook={false}
        enrollmentVersion={course.version}
        catalog={[course]}
        enrolled
        hasSession
        bookmarked={false}
        sources={[]}
        onEnroll={async () => {}}
        onUpgrade={async () => {}}
        onBookmark={async () => {}}
      />,
    );

    expect(
      await screen.findByRole("heading", { name: "Archived lesson" }),
    ).toBeInTheDocument();
    expect(
      screen.getByText("Archived package · read-only"),
    ).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Mark as read" })).toBeDisabled();
    expect(screen.getByRole("button", { name: "Save note" })).toBeDisabled();
    expect(
      screen.getByRole("link", { name: /Open the current course version/ }),
    ).toHaveAttribute("href", "#/course/cell-biology");
    expect(archivedCourseRequest).toHaveBeenCalledWith(
      "cell-biology",
      "0.34.0",
    );
    expect(archivedLessonRequest).toHaveBeenCalledWith(
      "cell-biology",
      "0.34.0",
      "lesson-one",
    );
    expect(currentCourseRequest).not.toHaveBeenCalled();
    expect(progressRequest).not.toHaveBeenCalled();
    expect(
      screen.queryByRole("link", { name: "Practice gradebook" }),
    ).toBeNull();
  });
});

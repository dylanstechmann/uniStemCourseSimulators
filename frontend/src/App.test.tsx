import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, describe, expect, it, vi } from "vitest";
import App from "./App";
import { api } from "./api";
import type {
  AssessmentPlan,
  Course,
  CurriculumMap,
  Gradebook,
  Lesson,
  ReviewQueue,
} from "./types";

afterEach(() => {
  window.location.hash = "";
});

describe("shared scientific tools route", () => {
  it("opens a calculator directly for a public reader", async () => {
    vi.spyOn(api, "session").mockResolvedValue({
      user: null,
      csrf_token: null,
    });
    vi.spyOn(api, "courses").mockResolvedValue([]);
    vi.spyOn(api, "sources").mockResolvedValue([]);
    vi.spyOn(api, "curriculum").mockResolvedValue({
      schema_version: "1.0",
      description: "Test map",
      nodes: [],
      pathways: [],
      alignment_maps: [],
    });
    window.location.hash = "/tools/diffusion";
    render(<App />);
    expect(
      await screen.findByRole("heading", { name: "Diffusion timescale" }),
    ).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Study tools" })).toHaveAttribute(
      "aria-current",
      "page",
    );
    await userEvent.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByText("10 s")).toBeInTheDocument();
  });
});

describe("reader keyboard navigation", () => {
  it("moves the skip-link focus to main without replacing the course route", async () => {
    const course: Course = {
      id: "cell-biology",
      title: "Foundations of Cell and Molecular Biology",
      description: "Reason about cell experiments.",
      domain: "Life sciences",
      level: "Year 1",
      maturity: "partial",
      version: "0.1",
      lesson_count: 4,
      limitations: ["This partial package is not a semester course."],
      prerequisites: {
        course_ids: [],
        recommended_course_ids: [],
        concurrent_course_ids: [],
        knowledge: ["High-school biology and chemistry"],
        statement: "Review basic molecular structure before beginning.",
      },
      outcomes: [],
      lesson_objectives: [],
      modules: [],
      weeks: [],
      syllabus_markdown: "Original partial syllabus.",
      license: "CC-BY-4.0",
      review_status: {},
      assessment_policy: {},
    };
    vi.spyOn(api, "session").mockResolvedValue({
      user: null,
      csrf_token: null,
    });
    vi.spyOn(api, "courses").mockResolvedValue([course]);
    vi.spyOn(api, "sources").mockResolvedValue([]);
    vi.spyOn(api, "curriculum").mockResolvedValue({
      schema_version: "1.0",
      description: "A planning map for this route test.",
      nodes: [],
      pathways: [],
      alignment_maps: [],
    } satisfies CurriculumMap);
    vi.spyOn(api, "course").mockResolvedValue(course);
    const scroll = vi.fn();
    Object.defineProperty(Element.prototype, "scrollIntoView", {
      configurable: true,
      value: scroll,
    });
    window.location.hash = "/course/cell-biology";
    render(<App />);
    await screen.findByRole("heading", {
      name: course.title,
      level: 1,
    });
    const originalRoute = window.location.hash;
    await userEvent.click(
      screen.getByRole("link", { name: "Skip to main content" }),
    );
    expect(window.location.hash).toBe(originalRoute);
    expect(screen.getByRole("main")).toHaveFocus();
    expect(scroll).toHaveBeenCalledOnce();
    expect(
      screen.getByRole("heading", { name: course.title, level: 1 }),
    ).toBeInTheDocument();
  });

  it("parses a scheduled activity URL and opens the matching enrolled practice set", async () => {
    const course: Course = {
      id: "cell-biology",
      title: "Foundations of Cell and Molecular Biology",
      description: "Reason about cell experiments.",
      domain: "Life sciences",
      level: "Year 1",
      maturity: "partial",
      version: "0.35.0",
      lesson_count: 0,
      limitations: ["This partial package is not a semester course."],
      prerequisites: {
        course_ids: [],
        recommended_course_ids: [],
        concurrent_course_ids: [],
        knowledge: [],
        statement: "No prerequisites for this route fixture.",
      },
      outcomes: [],
      lesson_objectives: [],
      modules: [],
      weeks: [],
      syllabus_markdown: "Test syllabus.",
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
          objective_count: 0,
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
      limitations: "Practice does not establish course completion.",
    };
    const reviewQueue: ReviewQueue = {
      course_id: course.id,
      content_version: course.version,
      policy_version: "retrieval-schedule-v1",
      policy: "Self-rated retrieval.",
      generated_at: "2026-10-10T12:00:00Z",
      counts: { due: 0, new: 0, upcoming: 0 },
      due: [],
      new: [],
      upcoming: [],
      limitations: "Self-ratings are not grades.",
    };

    vi.spyOn(api, "session").mockResolvedValue({
      user: { id: "guest-1", email: null, is_guest: true },
      csrf_token: "fixture-csrf-token",
    });
    vi.spyOn(api, "courses").mockResolvedValue([course]);
    vi.spyOn(api, "sources").mockResolvedValue([]);
    vi.spyOn(api, "curriculum").mockResolvedValue({
      schema_version: "1.0",
      description: "A route-test map.",
      nodes: [],
      pathways: [],
      alignment_maps: [],
    } satisfies CurriculumMap);
    vi.spyOn(api, "enrollments").mockResolvedValue([
      {
        course_id: course.id,
        content_version: course.version,
        created_at: "2026-10-10T12:00:00Z",
      },
    ]);
    vi.spyOn(api, "bookmarks").mockResolvedValue([]);
    vi.spyOn(api, "course").mockResolvedValue(course);
    vi.spyOn(api, "progress").mockResolvedValue([]);
    vi.spyOn(api, "notes").mockResolvedValue([]);
    vi.spyOn(api, "attempts").mockResolvedValue([]);
    vi.spyOn(api, "gradebook").mockResolvedValue(gradebook);
    vi.spyOn(api, "assessmentPlan").mockResolvedValue(assessmentPlan);
    vi.spyOn(api, "gradedSubmissions").mockResolvedValue([]);
    vi.spyOn(api, "reviewQueue").mockResolvedValue(reviewQueue);
    vi.spyOn(api, "archivedCourseVersions").mockResolvedValue([]);
    vi.spyOn(api, "practiceAssessment").mockResolvedValue({
      course_id: course.id,
      assessment_id: "practice-one",
      title: "Control-selection practice",
      content_version: course.version,
      points: 1,
      questions: [],
    });

    window.location.hash =
      "/course/cell-biology/gradebook/assessment/practice-one";
    render(<App />);

    expect(
      await screen.findByRole("heading", {
        name: "Control-selection practice",
        level: 2,
      }),
    ).toBeInTheDocument();
  });

  it("parses an enrolled archived-version lesson route as read-only content", async () => {
    const current: Course = {
      id: "cell-biology",
      title: "Foundations of Cell and Molecular Biology",
      description: "Reason about cell experiments.",
      domain: "Life sciences",
      level: "Year 1",
      maturity: "partial",
      version: "0.2.0",
      lesson_count: 1,
      limitations: [],
      prerequisites: {
        course_ids: [],
        recommended_course_ids: [],
        concurrent_course_ids: [],
        knowledge: [],
        statement: "",
      },
      outcomes: [],
      lesson_objectives: [],
      modules: [],
      weeks: [],
      syllabus_markdown: "Current syllabus.",
      license: "CC-BY-4.0",
      review_status: "unreviewed",
      assessment_policy: {},
    };
    const archived = { ...current, version: "0.1.0" };
    const lesson: Lesson = {
      id: "lesson-one",
      title: "Saved reading",
      markdown: "This is the archived reading text.",
      learning_objective_ids: [],
      source_ids: [],
      worked_example: "",
      questions: [],
      retrieval_cards: [],
    };
    vi.spyOn(api, "session").mockResolvedValue({
      user: { id: "guest-archive", email: null, is_guest: true },
      csrf_token: "fixture-csrf-token",
    });
    vi.spyOn(api, "courses").mockResolvedValue([current]);
    vi.spyOn(api, "sources").mockResolvedValue([]);
    vi.spyOn(api, "curriculum").mockResolvedValue({
      schema_version: "1.0",
      description: "A historical route test.",
      nodes: [],
      pathways: [],
      alignment_maps: [],
    } satisfies CurriculumMap);
    vi.spyOn(api, "enrollments").mockResolvedValue([
      {
        course_id: current.id,
        content_version: current.version,
        created_at: "2026-10-10T12:00:00Z",
      },
    ]);
    vi.spyOn(api, "bookmarks").mockResolvedValue([]);
    const archivedCourseRequest = vi
      .spyOn(api, "archivedCourse")
      .mockResolvedValue(archived);
    const archivedLessonRequest = vi
      .spyOn(api, "archivedLesson")
      .mockResolvedValue(lesson);
    const currentCourseRequest = vi.spyOn(api, "course");

    window.location.hash =
      "/course/cell-biology/version/0.1.0/lesson/lesson-one";
    render(<App />);

    expect(
      await screen.findByText("This is the archived reading text."),
    ).toBeInTheDocument();
    expect(
      screen.getByText("Archived package · read-only"),
    ).toBeInTheDocument();
    expect(archivedCourseRequest).toHaveBeenCalledWith("cell-biology", "0.1.0");
    expect(archivedLessonRequest).toHaveBeenCalledWith(
      "cell-biology",
      "0.1.0",
      "lesson-one",
    );
    expect(currentCourseRequest).not.toHaveBeenCalled();
  });
});

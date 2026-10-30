import type {
  Attempt,
  BenchAction,
  BenchProtocol,
  BenchProtocolSummary,
  BenchRun,
  CardRating,
  CardReviewResult,
  CaseDraft,
  Course,
  CurriculumMap,
  CourseSummary,
  Enrollment,
  Appeal,
  AssessmentAnswer,
  AssessmentPlan,
  InstructorAppeal,
  GradedSubmissionAppeal,
  InstructorGradedSubmissionAppeal,
  Gradebook,
  GradedAssessment,
  GradedSubmission,
  Lesson,
  Note,
  NotebookPage,
  Progress,
  PracticeAssessment,
  ReviewQueue,
  Session,
  Source,
} from "./types";

const base = "/api/v1";
let csrfToken: string | null = null;

export class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

async function request<T>(
  path: string,
  method = "GET",
  body?: unknown,
): Promise<T> {
  const headers: Record<string, string> = { Accept: "application/json" };
  if (body !== undefined) headers["Content-Type"] = "application/json";
  if (method !== "GET" && csrfToken) headers["X-CSRF-Token"] = csrfToken;
  const response = await fetch(`${base}${path}`, {
    method,
    credentials: "include",
    headers,
    ...(body !== undefined ? { body: JSON.stringify(body) } : {}),
  });
  if (!response.ok) {
    const error = (await response.json().catch(() => ({}))) as {
      detail?: unknown;
    };
    const message =
      typeof error.detail === "string"
        ? error.detail
        : `Request failed (${response.status}). Please review your input or try again.`;
    throw new ApiError(message, response.status);
  }
  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}

const encode = encodeURIComponent;
export const api = {
  async session() {
    const session = await request<Session>("/auth/session");
    csrfToken = session.csrf_token;
    return session;
  },
  async guest() {
    await request("/auth/guest", "POST", {});
    return this.session();
  },
  async register(email: string, password: string) {
    await request("/auth/register", "POST", { email, password });
    return this.session();
  },
  async login(email: string, password: string) {
    await request("/auth/login", "POST", { email, password });
    return this.session();
  },
  async logout() {
    await request("/auth/logout", "POST");
    csrfToken = null;
  },
  courses: () => request<CourseSummary[]>("/courses"),
  benchProtocols: () => request<BenchProtocolSummary[]>("/bench/protocols"),
  benchProtocol: (id: string) =>
    request<BenchProtocol>(`/bench/protocols/${encode(id)}`),
  benchReplay: (
    id: string,
    seed: number,
    mode: "guided" | "practice",
    actions: BenchAction[],
  ) =>
    request<BenchRun>(`/bench/protocols/${encode(id)}/replay`, "POST", {
      seed,
      mode,
      actions,
    }),
  curriculum: () => request<CurriculumMap>("/curriculum"),
  course: (id: string) => request<Course>(`/courses/${encode(id)}`),
  archivedCourseVersions: (id: string) =>
    request<string[]>(`/courses/${encode(id)}/versions`),
  archivedCourse: (id: string, version: string) =>
    request<Course>(`/courses/${encode(id)}/versions/${encode(version)}`),
  lesson: (id: string, lesson: string) =>
    request<Lesson>(`/courses/${encode(id)}/lessons/${encode(lesson)}`),
  archivedLesson: (id: string, version: string, lesson: string) =>
    request<Lesson>(
      `/courses/${encode(id)}/versions/${encode(version)}/lessons/${encode(lesson)}`,
    ),
  sources: () => request<Source[]>("/sources"),
  enrollments: () => request<Enrollment[]>("/enrollments"),
  enroll: (course_id: string) =>
    request<Enrollment>("/enrollments", "POST", { course_id }),
  upgradeEnrollment: (id: string) =>
    request<Enrollment>(`/enrollments/${encode(id)}/version`, "PUT", {}),
  assessmentPlan: (id: string) =>
    request<AssessmentPlan>(`/assessments/${encode(id)}`),
  gradedAssessment: (id: string, assessmentId: string) =>
    request<GradedAssessment>(
      `/assessments/${encode(id)}/${encode(assessmentId)}/questions`,
    ),
  practiceAssessment: (id: string, assessmentId: string) =>
    request<PracticeAssessment>(
      `/assessments/${encode(id)}/${encode(assessmentId)}/practice-questions`,
    ),
  submitGradedAssessment: (
    id: string,
    assessmentId: string,
    responses: Record<string, AssessmentAnswer>,
    assignmentToken?: string | null,
  ) =>
    request<GradedSubmission>(
      `/assessments/${encode(id)}/${encode(assessmentId)}/submissions`,
      "POST",
      {
        responses,
        ...(assignmentToken ? { assignment_token: assignmentToken } : {}),
      },
    ),
  gradedSubmissions: (id: string) =>
    request<GradedSubmission[]>(`/assessments/${encode(id)}/submissions`),
  requestGradedAppeal: (submissionId: string, reason: string) =>
    request<GradedSubmissionAppeal>(
      `/graded-submissions/${encode(submissionId)}/appeals`,
      "POST",
      { reason },
    ),
  gradedAppeals: () => request<GradedSubmissionAppeal[]>("/graded-appeals"),
  instructorGradedAppeals: (status = "open") =>
    request<InstructorGradedSubmissionAppeal[]>(
      `/instructor/graded-appeals?status=${encode(status)}`,
    ),
  reviewGradedAppeal: (
    appealId: string,
    decision: "adjusted" | "upheld" | "declined",
    review_note: string,
    override_score?: number,
  ) =>
    request<InstructorGradedSubmissionAppeal>(
      `/instructor/graded-appeals/${encode(appealId)}/review`,
      "POST",
      {
        decision,
        review_note,
        ...(override_score !== undefined ? { override_score } : {}),
      },
    ),
  progress: (id: string) => request<Progress[]>(`/progress/${encode(id)}`),
  setProgress: (id: string, lesson: string, completed: boolean) =>
    request<Progress>(`/progress/${encode(id)}/${encode(lesson)}`, "PATCH", {
      completed,
    }),
  notes: (id: string) => request<Note[]>(`/notes/${encode(id)}`),
  notebook: (query: string, courseId?: string, offset = 0) => {
    const params = new URLSearchParams({ q: query, offset: String(offset) });
    if (courseId) params.set("course_id", courseId);
    return request<NotebookPage>(`/notes?${params.toString()}`);
  },
  saveNote: (id: string, lesson: string, body: string) =>
    request<Note>(`/notes/${encode(id)}/${encode(lesson)}`, "PUT", { body }),
  caseDrafts: (id: string) =>
    request<CaseDraft[]>(`/case-drafts/${encode(id)}`),
  saveCaseDraft: (
    id: string,
    caseId: string,
    body: {
      content_version: string;
      case_sha256: string;
      response: string;
      checked_criteria: string[];
      expected_revision: number;
    },
  ) =>
    request<CaseDraft>(
      `/case-drafts/${encode(id)}/${encode(caseId)}`,
      "PUT",
      body,
    ),
  bookmarks: () => request<string[]>("/bookmarks"),
  bookmark: (id: string, saved: boolean) =>
    request(`/bookmarks/${encode(id)}`, "PUT", { saved }),
  attempt: (
    id: string,
    question: string,
    response: string | number | number[] | Record<string, string>,
    unit?: string,
    variantToken?: string | null,
  ) =>
    request<Attempt>(
      `/courses/${encode(id)}/questions/${encode(question)}/attempts`,
      "POST",
      {
        response,
        ...(unit ? { unit } : {}),
        ...(variantToken ? { variant_token: variantToken } : {}),
      },
    ),
  attempts: (id: string) =>
    request<Attempt[]>(`/attempts?course_id=${encode(id)}`),
  requestAppeal: (attemptId: string, reason: string) =>
    request<Appeal>(`/attempts/${encode(attemptId)}/appeals`, "POST", {
      reason,
    }),
  instructorAppeals: (status = "open") =>
    request<InstructorAppeal[]>(`/instructor/appeals?status=${encode(status)}`),
  reviewAppeal: (
    appealId: string,
    decision: "adjusted" | "upheld" | "declined",
    review_note: string,
    override_score?: number,
  ) =>
    request<InstructorAppeal>(
      `/instructor/appeals/${encode(appealId)}/review`,
      "POST",
      {
        decision,
        review_note,
        ...(override_score !== undefined ? { override_score } : {}),
      },
    ),
  gradebook: (id: string) => request<Gradebook>(`/gradebook/${encode(id)}`),
  reviewQueue: (id: string) => request<ReviewQueue>(`/reviews/${encode(id)}`),
  reviewCard: (id: string, cardId: string, rating: CardRating) =>
    request<CardReviewResult>(
      `/courses/${encode(id)}/cards/${encode(cardId)}/reviews`,
      "POST",
      { rating },
    ),
  exportData: () => request<unknown>("/learner/export"),
  async deleteLearner() {
    await request("/learner", "DELETE");
    csrfToken = null;
  },
};

export function errorMessage(error: unknown): string {
  return error instanceof Error
    ? error.message
    : "Unable to complete this action. Please try again.";
}

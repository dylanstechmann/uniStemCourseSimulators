export type Maturity =
  | "catalog-only"
  | "outlined"
  | "partial"
  | "beta"
  | "complete"
  | "externally reviewed";
export interface User {
  id: string;
  email: string | null;
  is_guest: boolean;
}
export interface Session {
  user: User | null;
  csrf_token: string | null;
  can_review?: boolean;
}
export interface CourseSummary {
  id: string;
  title: string;
  description: string;
  domain: string;
  level: string;
  maturity: Maturity;
  version: string;
  lesson_count: number;
  limitations: string[];
}
export interface CurriculumNode {
  id: string;
  title: string;
  domain: string;
  level: string;
  maturity: Maturity;
  description: string;
  prerequisites: {
    course_ids: string[];
    recommended_course_ids: string[];
    concurrent_course_ids: string[];
    knowledge: string[];
    statement: string;
  };
  package_id: string | null;
  related_package_ids: string[];
  relation_note: string | null;
}
export interface CurriculumPathway {
  id: string;
  title: string;
  description: string;
  course_ids: string[];
  source_ids: string[];
  sequence_note: string;
}
export interface CurriculumMap {
  schema_version: string;
  description: string;
  nodes: CurriculumNode[];
  pathways: CurriculumPathway[];
  alignment_maps: {
    id: string;
    title: string;
    source_ids: string[];
    foundational_nodes: string[];
    advanced_nodes: string[];
    disclaimer: string;
  }[];
}
export interface LearningObjective {
  id: string;
  description: string;
  bloom: string;
}
export interface CourseWeek {
  week: number;
  title: string;
  lessons: { id: string; title: string }[];
  assessments: {
    id: string;
    title: string;
    type: string;
    mode: "practice" | "graded" | "self-assessment";
  }[];
}
export interface LessonSummary {
  id: string;
  title: string;
  learning_objective_ids: string[];
}
export interface CaseStudy {
  id: string;
  prompt: string;
  mode: "self-assessment";
  objective_ids: string[];
  criteria: { id: string; criterion: string }[];
  limitations: string[];
  case_sha256: string;
}

export interface CaseDraft {
  id: string;
  course_id: string;
  case_id: string;
  content_version: string;
  case_sha256: string;
  case_snapshot: CaseStudy;
  response: string;
  checked_criteria: string[];
  revision: number;
  updated_at: string;
}

export interface Course extends CourseSummary {
  prerequisites: {
    course_ids: string[];
    recommended_course_ids: string[];
    concurrent_course_ids: string[];
    knowledge: string[];
    statement: string;
  };
  outcomes: LearningObjective[];
  lesson_objectives: LearningObjective[];
  modules: {
    id: string;
    title: string;
    source_ids: string[];
    lessons: LessonSummary[];
  }[];
  weeks: CourseWeek[];
  case_studies?: CaseStudy[];
  syllabus_markdown: string;
  license: string;
  review_status: unknown;
  assessment_policy: unknown;
}
export interface Question {
  id: string;
  type:
    | "single_choice"
    | "multiple_select"
    | "numeric"
    | "symbolic"
    | "structured"
    | "data_interpretation"
    | "graph"
    | "file_upload";
  prompt: string;
  options: string[];
  unit?: string;
  significant_figures?: number | null;
  points: number;
  selection?: "single" | "multiple";
  partial_credit_policy?: string | null;
  response_fields?: {
    id: string;
    type: "single_choice" | "numeric";
    prompt: string;
    options: string[];
    unit?: string | null;
    points: number;
  }[];
  graph_spec?: {
    x_axis: { label: string; minimum: number; maximum: number };
    y_axis: { label: string; minimum: number; maximum: number };
    points: { id: string; label: string }[];
    observations: { id: string; x: number; values: number[] }[];
  } | null;
  accepted_media_types?: string[];
  max_upload_bytes?: number | null;
  variant_id?: string | null;
  variant_token?: string | null;
  learning_objective_ids: string[];
  assessment_role: "formative" | "graded";
}
export interface Lesson {
  id: string;
  title: string;
  markdown: string;
  learning_objective_ids: string[];
  source_ids: string[];
  worked_example: string;
  questions: Question[];
  retrieval_cards: {
    id: string;
    front: string;
    back: string;
    learning_objective_ids: string[];
  }[];
}
export interface Enrollment {
  course_id: string;
  content_version: string;
  created_at: string;
}
export interface AssessmentPlan {
  course_id: string;
  content_version: string;
  grading_mode: "formative-only" | "graded-course";
  course_grade_status:
    | "not_configured"
    | "configured_no_submissions"
    | "configured_with_submissions";
  categories: { id: string; title: string | null; weight: number }[];
  category_aggregation: "points" | "assessment-average";
  attempt_policy: string;
  solution_release: string;
  late_policy: string;
  appeals: string;
  assessment_protection?: "protected" | "open";
  assessments: {
    id: string;
    title: string;
    type: string;
    mode: "practice" | "graded" | "self-assessment";
    category_id: string | null;
    week: number | null;
    points: number;
    item_count: number;
    objective_count: number;
    release_at: string | null;
    due_at: string | null;
    attempt_limit: number | null;
    attempt_scoring: "highest" | "latest";
    schedule_status: "practice" | "upcoming" | "open" | "closed";
  }[];
}
export interface PracticeAssessment {
  course_id: string;
  assessment_id: string;
  title: string;
  content_version: string;
  points: number;
  questions: Question[];
}
export interface Progress {
  lesson_id: string;
  completed: boolean;
  evidence: "learner-marked";
  updated_at?: string;
}
export interface Note {
  lesson_id: string;
  body: string;
  updated_at?: string;
}
export interface NotebookNote {
  course_id: string;
  course_title: string;
  lesson_id: string;
  lesson_title: string;
  body: string;
  updated_at: string;
}
export interface NotebookPage {
  items: NotebookNote[];
  total: number;
  offset: number;
  limit: number;
}
export interface Feedback {
  diagnosis: string;
  hint?: string;
  misconception: string | null;
  next_step: string;
  lesson_id: string | null;
  reasoning_assessed: boolean;
  provisional: boolean;
  components?: {
    field_id: string;
    label: string;
    score: number;
    max_score: number;
    diagnosis: string;
  }[];
}
export interface Attempt {
  id: string;
  course_id: string;
  question_id: string;
  content_version: string;
  response: {
    response: string | number | number[] | Record<string, string>;
    unit?: string;
    variant_id?: string;
  };
  score: number;
  effective_score: number;
  max_score: number;
  appeal: Appeal | null;
  result: {
    score: number;
    max_score: number;
    correct: boolean;
    assessment_role: "formative";
    grading_policy_version: string;
    feedback: Feedback;
  };
  objective_ids: string[];
  created_at: string;
}
export interface Appeal {
  id: string;
  attempt_id: string;
  course_id: string;
  question_id: string;
  reason: string;
  status: "open" | "adjusted" | "upheld" | "declined";
  decision: "adjusted" | "upheld" | "declined" | null;
  review_note: string | null;
  original_score: number;
  effective_score: number;
  max_score: number;
  created_at: string;
  reviewed_at: string | null;
}
export interface InstructorAppeal extends Appeal {
  learner: string;
  content_is_current: boolean;
  review_question: Question | null;
  question_prompt: string | null;
  question_options: string[] | null;
  response: Attempt["response"];
  automatic_feedback: Attempt["result"];
  specification_pinned: boolean;
}
export interface Gradebook {
  course_id: string;
  assessment_role: "formative";
  aggregation: string;
  score: number;
  max_score: number;
  attempt_count: number;
  manual_override_count: number;
  objective_evidence_policy: {
    version: "practice-evidence-v1";
    minimum_distinct_items: number;
    minimum_item_coverage: number;
    minimum_performance: number;
  };
  objective_evidence: Record<
    string,
    {
      attempts: number;
      correct_results: number;
      attempted_items: number;
      item_count: number;
      best_score: number;
      best_possible_score: number;
      performance: number | null;
      status:
        | "no_items"
        | "no_evidence"
        | "insufficient_evidence"
        | "needs_practice"
        | "provisional_practice_mastery";
    }
  >;
  limitations: string;
  course_grade?: {
    score_percent: number | null;
    category_scores: Record<string, number | null>;
    active_weight: number;
    policy_version: "weighted-grade-v1";
    manual_override_count: number;
    status: "configured_no_submissions" | "in_progress";
    explanation: string;
  } | null;
}
export type AssessmentAnswer = {
  response: string | number | number[] | Record<string, string>;
  unit?: string;
};
export interface GradedAssessment {
  course_id: string;
  assessment_id: string;
  title: string;
  content_version: string;
  points: number;
  questions: Question[];
  attempts_used: number;
  attempt_limit: number | null;
  schedule_status: "open" | "closed";
  assignment_token?: string | null;
}
export interface GradedSubmission {
  id: string;
  course_id: string;
  assessment_id: string;
  content_version: string;
  attempt_number: number;
  responses: Record<string, AssessmentAnswer>;
  results: {
    question_id: string;
    variant_id?: string | null;
    score: number;
    max_score: number;
    feedback: Feedback;
  }[];
  score: number;
  effective_score: number;
  max_score: number;
  score_percent: number;
  effective_score_percent: number;
  submitted_at: string;
  appeal: GradedSubmissionAppeal | null;
}
export interface GradedSubmissionAppeal {
  id: string;
  submission_id: string;
  course_id: string;
  assessment_id: string;
  attempt_number: number;
  reason: string;
  status: "open" | "adjusted" | "upheld" | "declined";
  decision: "adjusted" | "upheld" | "declined" | null;
  review_note: string | null;
  original_score: number;
  effective_score: number;
  max_score: number;
  created_at: string;
  reviewed_at: string | null;
}
export interface InstructorGradedSubmissionAppeal extends GradedSubmissionAppeal {
  learner: string;
  specification_verified: boolean;
  assessment_title: string;
  questions: Question[] | null;
  responses: Record<string, AssessmentAnswer>;
  automatic_results: GradedSubmission["results"];
  specification_pinned: boolean;
}
export interface Source {
  id: string;
  title: string;
  url: string;
  institution: string;
  license?: string;
}
export type CardRating = "again" | "hard" | "good" | "easy";
export interface CardSchedule {
  policy_version: string;
  last_rating: CardRating;
  review_count: number;
  repetitions: number;
  ease: number;
  interval_days: number;
  due_at: string;
  reviewed_at: string;
  due: boolean;
}
export interface ReviewQueueCard {
  card_id: string;
  lesson_id: string;
  lesson_title: string;
  front: string;
  back: string;
  learning_objective_ids: string[];
  schedule: CardSchedule | null;
  content_changed_since_last_review: boolean;
}
export interface ReviewQueue {
  course_id: string;
  content_version: string;
  policy_version: string;
  policy: string;
  generated_at: string;
  counts: { due: number; new: number; upcoming: number };
  due: ReviewQueueCard[];
  new: ReviewQueueCard[];
  upcoming: ReviewQueueCard[];
  limitations: string;
}
export interface CardReviewResult {
  card_id: string;
  lesson_id: string;
  rating: CardRating;
  schedule: CardSchedule;
}

export interface BenchProtocolSummary {
  id: string;
  version: string;
  title: string;
  layer: number;
  summary: string;
}

export interface BenchParam {
  name: string;
  label: string;
  type: "number" | "integer" | "boolean" | "choice";
  min?: number;
  max?: number;
  unit?: string;
  options?: { value: string; label: string }[];
}

export interface BenchActionSpec {
  name: string;
  label: string;
  params: BenchParam[];
}

export interface BenchProtocol extends BenchProtocolSummary {
  scenario: string;
  actions: BenchActionSpec[];
  limitations: string[];
  sources: { source_id: string; use: string }[];
}

export type BenchParamValue = string | number | boolean;

export interface BenchAction {
  name: string;
  params: Record<string, BenchParamValue>;
}

export interface BenchEvent {
  kind: "info" | "readout" | "warning" | "consequence";
  text: string;
  data: Record<string, unknown>;
}

export interface BenchCheckpoint {
  id: string;
  severity: "critical" | "major" | "minor";
  description: string;
  rationale: string;
  source: {
    kind: string;
    source_id?: string;
    location?: string;
    note?: string;
  };
  met: boolean | null;
  detail: string;
}

export interface BenchRun {
  protocol_id: string;
  protocol_version: string;
  seed: number;
  mode: "guided" | "practice";
  finished: boolean;
  clock_minutes: number;
  panels: { title: string; rows: [string, string][] }[];
  log: {
    index: number;
    name: string;
    label: string;
    params: Record<string, BenchParamValue>;
    clock_minutes: number;
    events: BenchEvent[];
  }[];
  guidance: string[] | null;
  debrief: {
    checkpoints: BenchCheckpoint[];
    missed: Record<"critical" | "major" | "minor", number>;
    met_count: number;
    applicable_count: number;
    all_critical_met: boolean;
    revealed: string[];
    note: string;
  } | null;
}

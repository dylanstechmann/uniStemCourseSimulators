import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import type { CourseWeek } from "../types";
import { CourseSchedule } from "./CourseSchedule";

const weeks: CourseWeek[] = [
  {
    week: 1,
    title: "Molecules and experimental controls",
    lessons: [{ id: "lesson-one", title: "Experimental controls" }],
    assessments: [
      {
        id: "practice-one",
        title: "Control-selection practice",
        type: "practice",
        mode: "practice",
      },
    ],
  },
  {
    week: 8,
    title: "Cumulative weeks 1–7 review (ungraded practice; no midterm)",
    lessons: [],
    assessments: [
      {
        id: "review",
        title: "Cumulative review",
        type: "practice",
        mode: "practice",
      },
    ],
  },
];

describe("typed course schedule", () => {
  it("shows week sequence, links lessons, and labels unmeasured timing honestly", () => {
    render(<CourseSchedule courseId="cell-biology" weeks={weeks} />);

    expect(
      screen.getByRole("heading", { name: "Course schedule" }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "Experimental controls" }),
    ).toHaveAttribute("href", "#/course/cell-biology/lesson/lesson-one");
    expect(
      screen.getByRole("link", { name: "Control-selection practice" }),
    ).toHaveAttribute(
      "href",
      "#/course/cell-biology/gradebook/assessment/practice-one",
    );
    expect(
      screen.getByRole("heading", {
        name: /Week 8: Cumulative weeks 1–7 review/,
      }),
    ).toBeInTheDocument();
    expect(
      screen.getByText("No lesson is scheduled this week."),
    ).toBeInTheDocument();
    expect(screen.getByText(/not calendar dates/)).toBeInTheDocument();
    expect(screen.getByText(/has not been measured/)).toBeInTheDocument();
  });

  it("omits the schedule section when the package has no authored weeks", () => {
    const { container } = render(
      <CourseSchedule courseId="fixture" weeks={[]} />,
    );
    expect(container).toBeEmptyDOMElement();
  });

  it("links an ungraded case to the studio in current and archived schedules", () => {
    const caseWeek: CourseWeek = {
      week: 14,
      title: "Integrative case",
      lessons: [],
      assessments: [
        {
          id: "case",
          title: "Transport case",
          type: "case",
          mode: "self-assessment",
        },
      ],
    };
    const { rerender } = render(
      <CourseSchedule courseId="cell-biology" weeks={[caseWeek]} />,
    );
    expect(
      screen.getByRole("link", { name: "Transport case" }),
    ).toHaveAttribute("href", "#/course/cell-biology/cases");
    rerender(
      <CourseSchedule
        courseId="cell-biology"
        weeks={[caseWeek]}
        linkPrefix="#/course/cell-biology/version/0.61.0"
        readOnly
      />,
    );
    expect(
      screen.getByRole("link", { name: "Transport case" }),
    ).toHaveAttribute("href", "#/course/cell-biology/version/0.61.0/cases");
  });
});

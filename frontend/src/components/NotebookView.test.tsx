import { afterEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { api } from "../api";
import type { CourseSummary, NotebookPage } from "../types";
import { NotebookView } from "./NotebookView";

afterEach(() => vi.restoreAllMocks());

const course: CourseSummary = {
  id: "cell-biology",
  title: "Foundations of Cell Biology",
  description: "A partial course.",
  domain: "Life sciences",
  level: "Year 1",
  maturity: "partial",
  version: "0.1.0",
  lesson_count: 1,
  limitations: [],
};

const page: NotebookPage = {
  items: [
    {
      course_id: course.id,
      course_title: course.title,
      lesson_id: "lesson-one",
      lesson_title: "Membranes and transport",
      body: "Use the matched vehicle control.\n<script>kept as plain text</script>",
      updated_at: "2026-10-11T12:00:00Z",
    },
  ],
  total: 1,
  offset: 0,
  limit: 50,
};

describe("cross-course notebook", () => {
  it("shows saved note text with a link back to its lesson and filters by search", async () => {
    const user = userEvent.setup();
    const request = vi.spyOn(api, "notebook").mockResolvedValue(page);
    render(
      <NotebookView hasSession courses={[course]} needsVersionReview={false} />,
    );

    expect(
      await screen.findByRole("link", { name: "Membranes and transport" }),
    ).toHaveAttribute("href", "#/course/cell-biology/lesson/lesson-one");
    // Keep the newline: the default normalizer would collapse it before matching.
    expect(
      screen.getByText(page.items[0].body, { normalizer: (text) => text }),
    ).toBeInTheDocument();
    expect(document.querySelector(".notebook-body script")).toBeNull();
    expect(screen.getByText("1 saved note")).toBeInTheDocument();

    await user.type(
      screen.getByRole("searchbox", { name: "Search saved note text" }),
      "vehicle",
    );
    await waitFor(() =>
      expect(request).toHaveBeenLastCalledWith("vehicle", undefined, 0),
    );
  });

  it("asks public readers to start a private session without requesting notes", () => {
    const request = vi.spyOn(api, "notebook");
    render(
      <NotebookView
        hasSession={false}
        courses={[]}
        needsVersionReview={false}
      />,
    );
    expect(
      screen.getByRole("link", { name: "Start a guest session or sign in" }),
    ).toHaveAttribute("href", "#/account");
    expect(request).not.toHaveBeenCalled();
  });
});

import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { api, ApiError } from "../api";
import type { CaseDraft, CaseStudy, Course } from "../types";
import { CaseStudio } from "./CaseStudio";

const study: CaseStudy = {
  id: "cell-biology:case",
  prompt: "Design a matched-control experiment.",
  mode: "self-assessment",
  objective_ids: [],
  criteria: [{ id: "control", criterion: "Uses a matched delivery control" }],
  limitations: ["An ungraded checklist."],
  case_sha256: "a".repeat(64),
};
const course = {
  id: "cell-biology",
  version: "0.61.0",
  case_studies: [study],
} as Course;
const draft: CaseDraft = {
  id: "draft-one",
  course_id: course.id,
  case_id: study.id,
  content_version: course.version,
  case_sha256: study.case_sha256,
  case_snapshot: study,
  response: "A saved response",
  checked_criteria: ["control"],
  revision: 1,
  updated_at: "2026-10-11T12:00:00Z",
};

describe("case studio", () => {
  it("shows the authored prompt to public readers without fetching private drafts", () => {
    const load = vi.spyOn(api, "caseDrafts");
    render(<CaseStudio course={course} enrolled={false} enabled={false} />);
    expect(screen.getByText(study.prompt)).toBeInTheDocument();
    expect(
      screen.getByRole("textbox", { name: "Your response" }),
    ).toBeDisabled();
    expect(screen.queryByRole("button", { name: "Save draft" })).toBeNull();
    expect(load).not.toHaveBeenCalled();
  });

  it("loads and saves a version-bound response and self-checks", async () => {
    vi.spyOn(api, "caseDrafts").mockResolvedValue([draft]);
    const save = vi.spyOn(api, "saveCaseDraft").mockResolvedValue({
      ...draft,
      revision: 2,
      response: "A saved response with new evidence",
      checked_criteria: [],
    });
    const user = userEvent.setup();
    render(<CaseStudio course={course} enrolled enabled />);
    const response = await screen.findByRole("textbox", {
      name: "Your response",
    });
    expect(response).toHaveValue(draft.response);
    expect(screen.getByRole("checkbox")).toBeChecked();
    expect(screen.getByRole("button", { name: "Save draft" })).toBeDisabled();
    await user.type(response, " with new evidence");
    await user.click(screen.getByRole("checkbox"));
    await user.click(screen.getByRole("button", { name: "Save draft" }));
    await screen.findByText(
      "Draft saved. Checklist marks record your own self-check.",
    );
    expect(save).toHaveBeenCalledWith(course.id, study.id, {
      content_version: course.version,
      case_sha256: study.case_sha256,
      response: "A saved response with new evidence",
      checked_criteria: [],
      expected_revision: 1,
    });
    expect(screen.getByText(/revision 2/)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Save draft" })).toBeDisabled();
  });

  it("retains unsaved text on conflict and waits for an explicit replacement", async () => {
    vi.spyOn(api, "caseDrafts")
      .mockResolvedValueOnce([draft])
      .mockResolvedValueOnce([
        { ...draft, response: "Other tab saved this", revision: 2 },
      ]);
    vi.spyOn(api, "saveCaseDraft").mockRejectedValue(
      new ApiError("The saved draft changed", 409),
    );
    const user = userEvent.setup();
    render(<CaseStudio course={course} enrolled enabled />);
    const response = await screen.findByRole("textbox", {
      name: "Your response",
    });
    await user.clear(response);
    await user.type(response, "My unsaved text");
    await user.click(screen.getByRole("button", { name: "Save draft" }));
    expect(await screen.findByRole("alert")).toHaveTextContent(
      "Your editor text is retained",
    );
    expect(response).toHaveValue("My unsaved text");
    expect(screen.getByRole("button", { name: "Save draft" })).toBeDisabled();
    await user.click(
      screen.getByRole("button", { name: "Replace editor with saved draft" }),
    );
    await waitFor(() =>
      expect(screen.getByRole("textbox")).toHaveValue("Other tab saved this"),
    );
  });

  it("keeps earlier prompts and text readable without treating markup as HTML", async () => {
    vi.spyOn(api, "caseDrafts").mockResolvedValue([
      {
        ...draft,
        case_sha256: "b".repeat(64),
        response: "<img src=x onerror=alert(1)>",
        case_snapshot: { ...study, prompt: "Earlier authored prompt" },
      },
    ]);
    render(<CaseStudio course={course} enrolled enabled />);
    expect(
      await screen.findByRole("region", { name: "Earlier case drafts" }),
    ).toBeInTheDocument();
    expect(screen.getByText("Earlier authored prompt")).toBeInTheDocument();
    expect(
      screen.getByText("<img src=x onerror=alert(1)>"),
    ).toBeInTheDocument();
    expect(screen.queryByRole("img")).toBeNull();
    expect(screen.getByRole("textbox")).toHaveValue("");
  });

  it("disables archived responses and current responses awaiting enrollment upgrade", async () => {
    vi.spyOn(api, "caseDrafts").mockResolvedValue([draft]);
    const { rerender } = render(
      <CaseStudio course={course} enrolled enabled={false} archived />,
    );
    expect(await screen.findByRole("textbox")).toHaveValue(draft.response);
    expect(screen.getByRole("textbox")).toBeDisabled();
    expect(
      screen.getByText(/archived case and its saved response are read-only/),
    ).toBeInTheDocument();
    rerender(<CaseStudio course={course} enrolled enabled={false} />);
    expect(screen.getByText(/Update your enrollment/)).toBeInTheDocument();
    expect(screen.getByRole("checkbox")).toBeDisabled();
  });

  it("does not enable editing after a draft-load failure and can retry", async () => {
    vi.spyOn(api, "caseDrafts")
      .mockRejectedValueOnce(new Error("Network unavailable"))
      .mockResolvedValueOnce([]);
    const user = userEvent.setup();
    render(<CaseStudio course={course} enrolled enabled />);
    expect(await screen.findByRole("alert")).toHaveTextContent(
      "Saving is disabled",
    );
    expect(screen.queryByRole("button", { name: "Save draft" })).toBeNull();
    await user.click(
      screen.getByRole("button", { name: "Retry loading drafts" }),
    );
    expect(await screen.findByRole("textbox")).toBeEnabled();
  });
});

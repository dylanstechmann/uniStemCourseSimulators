import { act, render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import type { Lesson, Note } from "../types";
import { LessonStudy } from "./LessonStudy";

const lesson: Lesson = {
  id: "lesson-one",
  title: "Experimental controls",
  markdown: "Choose a control before interpreting the result.",
  learning_objective_ids: [],
  source_ids: [],
  worked_example: "",
  questions: [],
  retrieval_cards: [],
};

const note: Note = {
  lesson_id: lesson.id,
  body: "Original note",
  updated_at: "2026-10-22T12:00:00Z",
};

function props() {
  return {
    lesson,
    enabled: true,
    completed: false,
    attempts: [],
    sources: [],
    onAttempt: vi.fn(),
    onAppeal: vi.fn(),
    onSaveNote: vi.fn().mockResolvedValue(undefined),
    onProgress: vi.fn().mockResolvedValue(undefined),
  };
}

describe("lesson note saving", () => {
  it("keeps edits made while a save is pending and lets the learner save them next", async () => {
    const user = userEvent.setup();
    let finishSave!: () => void;
    const saving = new Promise<void>((resolve) => {
      finishSave = resolve;
    });
    const callbacks = props();
    callbacks.onSaveNote.mockReturnValueOnce(saving);
    const { rerender } = render(<LessonStudy {...callbacks} note={note} />);
    const editor = screen.getByRole("textbox", { name: "Your private note" });

    await user.type(editor, " with first edit");
    await user.click(screen.getByRole("button", { name: "Save note" }));
    expect(callbacks.onSaveNote).toHaveBeenCalledWith(
      "Original note with first edit",
    );
    await user.type(editor, " and a newer edit");
    await act(async () => {
      rerender(
        <LessonStudy
          {...callbacks}
          note={{ ...note, body: "Original note with first edit" }}
        />,
      );
      finishSave();
      await saving;
    });

    expect(editor).toHaveValue(
      "Original note with first edit and a newer edit",
    );
    expect(screen.getByText("Unsaved changes.")).toBeInTheDocument();
    expect(screen.queryByText("Note saved.")).not.toBeInTheDocument();
    await user.click(screen.getByRole("button", { name: "Save note" }));
    expect(callbacks.onSaveNote).toHaveBeenLastCalledWith(
      "Original note with first edit and a newer edit",
    );
    expect(await screen.findByText("Note saved.")).toBeInTheDocument();
  });

  it("preserves a draft when the saved note arrives after the learner starts typing", async () => {
    const user = userEvent.setup();
    const callbacks = props();
    const { rerender } = render(<LessonStudy {...callbacks} />);
    const editor = screen.getByRole("textbox", { name: "Your private note" });
    await user.type(editor, "My new draft");

    rerender(<LessonStudy {...callbacks} note={note} />);
    expect(editor).toHaveValue("My new draft");
    expect(screen.getByText("Unsaved changes.")).toBeInTheDocument();
  });

  it("keeps a learner's undo while an earlier edit is being saved", async () => {
    const user = userEvent.setup();
    let finishSave!: () => void;
    const saving = new Promise<void>((resolve) => {
      finishSave = resolve;
    });
    const callbacks = props();
    callbacks.onSaveNote.mockReturnValueOnce(saving);
    const { rerender } = render(<LessonStudy {...callbacks} note={note} />);
    const editor = screen.getByRole("textbox", { name: "Your private note" });
    await user.type(editor, " revised");
    await user.click(screen.getByRole("button", { name: "Save note" }));
    await user.clear(editor);
    await user.type(editor, note.body);
    rerender(
      <LessonStudy
        {...callbacks}
        note={{ ...note, body: "Original note revised" }}
      />,
    );
    expect(editor).toHaveValue(note.body);
    await act(async () => {
      finishSave();
      await saving;
    });
    expect(editor).toHaveValue(note.body);
    expect(screen.getByText("Unsaved changes.")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Save note" })).toBeEnabled();
  });

  it("retains a failed save for retry and keeps reading progress independent", async () => {
    const user = userEvent.setup();
    const callbacks = props();
    callbacks.onSaveNote.mockRejectedValueOnce(new Error("Connection lost"));
    render(<LessonStudy {...callbacks} note={note} />);
    const editor = screen.getByRole("textbox", { name: "Your private note" });
    await user.type(editor, " revised");
    await user.click(screen.getByRole("button", { name: "Save note" }));
    expect(await screen.findByRole("alert")).toHaveTextContent(
      "Connection lost",
    );
    expect(editor).toHaveValue("Original note revised");

    await user.click(screen.getByRole("button", { name: "Mark as read" }));
    expect(callbacks.onProgress).toHaveBeenCalledWith(true);
    expect(screen.getByRole("button", { name: "Save note" })).toHaveTextContent(
      "Save note",
    );
    await user.click(screen.getByRole("button", { name: "Save note" }));
    await waitFor(() => expect(callbacks.onSaveNote).toHaveBeenCalledTimes(2));
    expect(await screen.findByText("Note saved.")).toBeInTheDocument();
  });
});

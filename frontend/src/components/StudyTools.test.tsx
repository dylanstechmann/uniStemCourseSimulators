import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";
import { StudyTools } from "./StudyTools";

describe("study tools", () => {
  it("calculates with the keyboard and clears stale results when an input changes", async () => {
    const user = userEvent.setup();
    render(<StudyTools toolId="enzyme" courses={[]} />);
    const substrate = screen.getByRole("spinbutton", {
      name: "Substrate concentration (μM)",
    });
    substrate.focus();
    await user.keyboard("{Enter}");
    expect(screen.getByText("66.6667 μM/min")).toBeInTheDocument();
    await user.clear(substrate);
    expect(screen.queryByText("66.6667 μM/min")).toBeNull();
    await user.type(substrate, "0");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByText("0 μM/min")).toBeInTheDocument();
    await user.click(screen.getByRole("button", { name: "Reset example" }));
    expect(substrate).toHaveValue(10);
    expect(screen.queryByText("0 μM/min")).toBeNull();
  });

  it("explains invalid inputs and resets fields when selecting another calculator", async () => {
    const user = userEvent.setup();
    const { rerender } = render(<StudyTools toolId="buffer" courses={[]} />);
    const acid = screen.getByRole("spinbutton", {
      name: "Conjugate-acid concentration (mM)",
    });
    await user.clear(acid);
    await user.type(acid, "0");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByRole("alert")).toHaveTextContent(
      "must be greater than 0",
    );
    rerender(<StudyTools toolId="rc" courses={[]} />);
    expect(screen.queryByRole("alert")).toBeNull();
    expect(
      screen.getByRole("spinbutton", { name: "Resistance (kΩ)" }),
    ).toHaveValue(100);
    expect(screen.getByRole("link", { name: "RC charging" })).toHaveAttribute(
      "aria-current",
      "page",
    );
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByText("1 s")).toBeInTheDocument();
    expect(screen.getByText("63.2121 %")).toBeInTheDocument();
  });
});

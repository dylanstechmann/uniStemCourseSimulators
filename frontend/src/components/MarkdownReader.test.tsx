import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { MarkdownReader } from "./MarkdownReader";

describe("MarkdownReader content boundary", () => {
  it("renders instructional Markdown without executing raw HTML or unsafe links", () => {
    const { container } = render(
      <MarkdownReader>
        {
          '## Experimental controls\n\nUse a [reference](https://example.edu).\n\n<script>window.stolen = true</script>\n\n<img src=x onerror="alert(1)">\n\n[unsafe](javascript:alert(1))'
        }
      </MarkdownReader>,
    );
    expect(
      screen.getByRole("heading", { name: "Experimental controls" }),
    ).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "reference" })).toHaveAttribute(
      "href",
      "https://example.edu",
    );
    expect(container.querySelector("script")).toBeNull();
    expect(container.querySelector("[onerror]")).toBeNull();
    expect(container.querySelector('a[href^="javascript:"]')).toBeNull();
  });

  it("renders Markdown tables with header cells and escaped pipes", () => {
    render(
      <MarkdownReader>
        {
          "| Hypothesis | P(unaffected \\| genotype) |\n| --- | ---: |\n| D/d | 0.10 |\n| d/d | 1 |"
        }
      </MarkdownReader>,
    );
    const table = screen.getByRole("table");
    expect(
      within(table)
        .getAllByRole("columnheader")
        .map((cell) => cell.textContent),
    ).toEqual(["Hypothesis", "P(unaffected | genotype)"]);
    expect(within(table).getAllByRole("row")).toHaveLength(3);
    expect(
      within(table).getByRole("cell", { name: "0.10" }),
    ).toBeInTheDocument();
  });

  it("makes scrollable code blocks keyboard focusable", () => {
    const { container } = render(
      <MarkdownReader>
        {"```csv\ncondition,measurement\ncontrol,12\n```"}
      </MarkdownReader>,
    );
    expect(container.querySelector("pre")).toHaveAttribute("tabindex", "0");
  });
});

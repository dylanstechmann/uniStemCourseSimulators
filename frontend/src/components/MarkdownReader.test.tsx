import { act, render, screen, waitFor, within } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import {
  MarkdownReader,
  containsMath,
  normalizeMathDelimiters,
} from "./MarkdownReader";

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

  it("renders inline and display LaTeX with KaTeX and keeps a MathML copy", async () => {
    const { container } = render(
      <MarkdownReader>
        {
          "Inline \\(K_m\\) and dollar $x^2$ forms.\n\n\\[\n\\frac{dC}{dt}=-kC\n\\]\n\nAfter."
        }
      </MarkdownReader>,
    );
    // Wait for the lazy math renderer, including its transitive imports, before checking the DOM.
    await act(() => vi.dynamicImportSettled());
    await waitFor(() =>
      expect(container.querySelectorAll(".katex")).toHaveLength(3),
    );
    expect(container.querySelectorAll(".katex-display")).toHaveLength(1);
    expect(container.querySelectorAll("math")).toHaveLength(3);
    // The TeX source survives only in the MathML annotation, not in the visible rendering.
    const visible = Array.from(container.querySelectorAll(".katex-html"))
      .map((node) => node.textContent)
      .join(" ");
    expect(visible).not.toContain("\\frac");
    expect(container.textContent).not.toContain("\\(");
    expect(container.querySelector(".katex-error")).toBeNull();
  });

  it("leaves delimiters inside code untouched", () => {
    expect(
      normalizeMathDelimiters(
        "Use `print(\\(x\\))` and \\(y\\).\n\n```\n\\[ z \\]\n```",
      ),
    ).toBe("Use `print(\\(x\\))` and $y$.\n\n```\n\\[ z \\]\n```");
    expect(normalizeMathDelimiters("  \\[\n  a=b\n  \\]")).toBe(
      "  $$\n  a=b\n  $$",
    );
    expect(containsMath("Plain text with `$HOME` in code.")).toBe(false);
    expect(containsMath("Rate \\(k\\).")).toBe(true);
  });
});

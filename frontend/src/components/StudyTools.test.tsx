import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";
import type { CourseSummary } from "../types";
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

  it("calculates the habitat example, resets it, and validates habitat constraints", async () => {
    const user = userEvent.setup();
    render(<StudyTools toolId="habitat-ledger" courses={[]} />);
    const ppfd = screen.getByRole("spinbutton", { name: "PPFD (μmol/m²/s)" });
    expect(ppfd).toHaveValue(200);
    expect(
      screen.getByRole("spinbutton", { name: "Photoperiod (h/day)" }),
    ).toHaveAttribute("max", "24");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    for (const value of [
      "11.52 mol/m²/day",
      "1.92 kWh/day",
      "3.84 kWh/day",
      "10 L/day",
      "75 %",
      "12 days",
    ])
      expect(screen.getByText(value, { exact: true })).toBeInTheDocument();

    await user.clear(ppfd);
    await user.type(ppfd, "400");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByText("23.04 mol/m²/day")).toBeInTheDocument();
    await user.click(screen.getByRole("button", { name: "Reset example" }));
    expect(ppfd).toHaveValue(200);
    expect(screen.queryByText("23.04 mol/m²/day")).toBeNull();

    const photoperiod = screen.getByRole("spinbutton", {
      name: "Photoperiod (h/day)",
    });
    await user.clear(photoperiod);
    await user.type(photoperiod, "25");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByRole("alert")).toHaveTextContent("must be at most 24");
    await user.click(screen.getByRole("button", { name: "Reset example" }));
    const recovered = screen.getByRole("spinbutton", {
      name: "Recovered water (L/day)",
    });
    await user.clear(recovered);
    await user.type(recovered, "41");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByRole("alert")).toHaveTextContent(
      "Recovered water cannot exceed water demand",
    );
  });

  it("omits endurance at full recovery and links the habitat course", async () => {
    const user = userEvent.setup();
    const courses: CourseSummary[] = [
      {
        id: "agriculture-construction-habitats",
        title: "Agriculture, Construction and Closed-Loop Habitats",
        description: "Audit synthetic habitat ledgers.",
        domain: "Agricultural, construction and habitat systems",
        level: "Year 2",
        maturity: "partial",
        version: "0.1.0",
        lesson_count: 8,
        limitations: ["Partial and unreviewed."],
      },
    ];
    render(<StudyTools toolId="habitat-ledger" courses={courses} />);
    const recovered = screen.getByRole("spinbutton", {
      name: "Recovered water (L/day)",
    });
    await user.clear(recovered);
    await user.type(recovered, "40");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByText("100 %", { exact: true })).toBeInTheDocument();
    expect(screen.queryByText("12 days", { exact: true })).toBeNull();
    expect(
      screen.getByRole("link", {
        name: "Agriculture, Construction and Closed-Loop Habitats",
      }),
    ).toHaveAttribute("href", "#/course/agriculture-construction-habitats");
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
    expect(
      screen.getByRole("link", { name: "RC charging and discharging" }),
    ).toHaveAttribute("aria-current", "page");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByText("1 s")).toBeInTheDocument();
    expect(screen.getByText("63.2121 %")).toBeInTheDocument();

    const time = screen.getByRole("spinbutton", { name: "Time (s)" });
    await user.clear(time);
    await user.type(time, "0.693147");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(
      screen.getByRole("heading", {
        name: "RC charging and discharging",
        exact: true,
      }),
    ).toBeVisible();
    expect(
      screen.getByText("Initial voltage remaining during discharge")
        .nextElementSibling,
    ).toHaveTextContent("50 %");
    expect(
      screen.getByText("Initial energy remaining during discharge")
        .nextElementSibling,
    ).toHaveTextContent("25 %");
  });
});

describe("materials and chemical engineering tools", () => {
  const course = (id: string, title: string): CourseSummary => ({
    id,
    title,
    description: "Synthetic course fixture.",
    domain: "Engineering",
    level: "Year 2",
    maturity: "partial",
    version: "0.1.0",
    lesson_count: 8,
    limitations: ["Unreviewed."],
  });

  it("calculates diffraction with Enter, links Materials Science and rejects the physical boundary", async () => {
    const user = userEvent.setup();
    render(
      <StudyTools
        toolId="crystal-diffraction"
        courses={[course("materials-science", "Materials Science")]}
      />,
    );
    expect(
      screen.getByRole("spinbutton", {
        name: "Cubic lattice parameter a (nm)",
      }),
    ).toHaveValue(0.4);
    await screen.getByRole("spinbutton", { name: "Wavelength λ (nm)" }).focus();
    await user.keyboard("{Enter}");
    expect(screen.getByText("0.4 nm", { exact: true })).toBeInTheDocument();
    expect(screen.getByText("11.0987 °", { exact: true })).toBeInTheDocument();
    expect(screen.getByText("22.1974 °", { exact: true })).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "Materials Science" }),
    ).toHaveAttribute("href", "#/course/materials-science");
    expect(
      screen.getByText(/Cubic, first-order toy model only/),
    ).toHaveTextContent("not phase identification");

    const wavelength = screen.getByRole("spinbutton", {
      name: "Wavelength λ (nm)",
    });
    await user.clear(wavelength);
    await user.type(wavelength, "0.81");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByRole("alert")).toHaveTextContent("cannot exceed 2d");
    expect(screen.queryByText("0.4 nm", { exact: true })).toBeNull();
    await user.click(screen.getByRole("button", { name: "Reset example" }));
    expect(wavelength).toHaveValue(0.154);
    expect(screen.queryByRole("alert")).toBeNull();
  });

  it("shows the complete stream balance, handles zero flow and rejects missing values", async () => {
    const user = userEvent.setup();
    render(
      <StudyTools
        toolId="stream-balance"
        courses={[
          course(
            "chemical-engineering-foundations",
            "Chemical Engineering Foundations",
          ),
        ]}
      />,
    );
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    for (const value of [
      "80 mol/h",
      "40 mol/h",
      "36 mol/h",
      "4 mol/h",
      "0 mol/h",
    ])
      expect(
        screen.getAllByText(value, { exact: true }).length,
      ).toBeGreaterThan(0);
    expect(screen.getByText("B unrecovered")).toBeInTheDocument();
    expect(screen.getByText("A balance closure residual")).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: "Chemical Engineering Foundations" }),
    ).toHaveAttribute("href", "#/course/chemical-engineering-foundations");

    const feed = screen.getByRole("spinbutton", {
      name: "Total feed flow (mol/h)",
    });
    await user.clear(feed);
    await user.type(feed, "0");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getAllByText("0 mol/h", { exact: true })).toHaveLength(6);
    await user.clear(feed);
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByRole("alert")).toHaveTextContent("finite number");
    await user.click(screen.getByRole("button", { name: "Reset example" }));
    expect(feed).toHaveValue(100);
  });

  it("requires an independence declaration before showing RSS and resets that declaration", async () => {
    const user = userEvent.setup();
    render(
      <StudyTools
        toolId="tolerance-stack"
        courses={[
          course(
            "materials-engineering-fabrication",
            "Materials Engineering for Fabrication",
          ),
        ]}
      />,
    );
    const model = screen.getByRole("combobox", { name: "RSS variation model" });
    expect(model).toHaveValue("not-declared");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByText("60 mm", { exact: true })).toBeInTheDocument();
    expect(screen.getByText("0.6 mm", { exact: true })).toBeInTheDocument();
    expect(screen.queryByText(/Conditional independent RSS/)).toBeNull();
    expect(screen.getByRole("status")).toHaveTextContent(
      "RSS is omitted because independent variation has not been declared",
    );

    await user.selectOptions(model, "independent");
    expect(screen.queryByText("60 mm", { exact: true })).toBeNull();
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(
      screen.getByText("0.374166 mm", { exact: true }),
    ).toBeInTheDocument();
    expect(screen.getByRole("status")).toHaveTextContent(
      "conditional on the declared independent-variation model",
    );
    expect(
      screen.getByRole("link", {
        name: "Materials Engineering for Fabrication",
      }),
    ).toHaveAttribute("href", "#/course/materials-engineering-fabrication");

    await user.click(screen.getByRole("button", { name: "Reset example" }));
    expect(model).toHaveValue("not-declared");
    expect(screen.queryByText("0.374166 mm", { exact: true })).toBeNull();
    const tolerance = screen.getByRole("spinbutton", {
      name: "Symmetric tolerance 1 (±mm)",
    });
    await user.clear(tolerance);
    await user.type(tolerance, "-0.1");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByRole("alert")).toHaveTextContent("at least 0");
  });

  it("omits unknown/unstable capability indices and shows stable arithmetic with both course links", async () => {
    const user = userEvent.setup();
    render(
      <StudyTools
        toolId="process-capability"
        courses={[
          course(
            "materials-engineering-fabrication",
            "Materials Engineering for Fabrication",
          ),
          course(
            "chemical-process-design-scale-up",
            "Chemical Process Design & Scale-Up",
          ),
        ]}
      />,
    );
    const state = screen.getByRole("combobox", {
      name: "Declared process state",
    });
    expect(state).toHaveValue("unknown");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.queryByText("Cp (declared stable process)")).toBeNull();
    expect(screen.getByRole("status")).toHaveTextContent(
      "omitted because process stability is unknown",
    );

    await user.selectOptions(state, "unstable");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.queryByText("Cpk (declared stable process)")).toBeNull();
    expect(screen.getByRole("status")).toHaveTextContent(
      "omitted because the process is declared unstable",
    );

    await user.selectOptions(state, "stable");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(
      screen.getByText("Cp (declared stable process)"),
    ).toBeInTheDocument();
    expect(
      screen.getByText("Cpk (declared stable process)"),
    ).toBeInTheDocument();
    expect(screen.getAllByText("1.66667", { exact: true })).toHaveLength(2);
    expect(screen.getByRole("status")).not.toHaveTextContent(
      "release-approved",
    );
    for (const title of [
      "Materials Engineering for Fabrication",
      "Chemical Process Design & Scale-Up",
    ])
      expect(screen.getByRole("link", { name: title })).toBeVisible();

    const lsl = screen.getByRole("spinbutton", {
      name: "Lower specification limit (LSL)",
    });
    await user.clear(lsl);
    await user.type(lsl, "60");
    await user.click(screen.getByRole("button", { name: "Calculate" }));
    expect(screen.getByRole("alert")).toHaveTextContent("less than USL");
    await user.click(screen.getByRole("button", { name: "Reset example" }));
    expect(state).toHaveValue("unknown");
    expect(lsl).toHaveValue(40);
  });
});

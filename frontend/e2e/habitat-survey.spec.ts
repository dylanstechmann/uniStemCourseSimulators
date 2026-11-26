import AxeBuilder from "@axe-core/playwright";
import { expect, test, type Page } from "@playwright/test";
import { readFile } from "node:fs/promises";

const courseId = "agriculture-construction-habitats";
const courseTitle =
  "Agriculture, Construction and Closed-Loop Habitats (partial interdisciplinary survey)";
const pathwayTitle = "Agriculture, Construction and Habitat Systems";

const lessons = [
  {
    id: `${courseId}-1`,
    title: "Agricultural systems, inventories and site boundaries",
    evidence: "closing stock = opening stock + inputs − outputs",
  },
  {
    id: `${courseId}-2`,
    title: "PPFD, DLI, photoperiod, timers and lighting energy",
    evidence: "DLI = PPFD × hours × 3600 / 1,000,000.",
  },
  {
    id: `${courseId}-3`,
    title: "Water and nutrient inventories, climate sensors and control",
    evidence: "no nutrient formulation",
  },
  {
    id: `${courseId}-4`,
    title: "Plant base-editing evidence: controls, comparators and limitations",
    evidence: "2025 correction",
  },
  {
    id: `${courseId}-5`,
    title:
      "Conceptual load paths, work breakdown and construction dependencies",
    evidence: "A sketch does not demonstrate capacity.",
  },
  {
    id: `${courseId}-6`,
    title: "Closed-loop habitat energy, water and outage balances",
    evidence: "not a life-support design",
  },
  {
    id: `${courseId}-7`,
    title: "Synthetic-data habitat audit lab",
    evidence: "habitat-audit.csv",
    resources: ["labs/habitat-audit.csv"],
  },
  {
    id: `${courseId}-project-guide`,
    title:
      "Optional integrative project guide: bounded habitat evidence package",
    evidence: "five linked milestone records",
    resources: [
      "labs/habitat-audit.csv",
      "assignments/habitat-project-rehearsal.csv",
    ],
  },
];

function monitorApiWrites(page: Page) {
  const writes: string[] = [];
  page.on("request", (request) => {
    if (
      request.url().includes("/api/") &&
      !["GET", "HEAD", "OPTIONS"].includes(request.method())
    )
      writes.push(request.url());
  });
  return writes;
}

async function expectBasicAccessibility(page: Page) {
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);
}

test("catalog, pathway, all lesson routes, synthetic CSVs and cases are public", async ({
  page,
}) => {
  const writes = monitorApiWrites(page);
  await page.goto("/");
  const search = page.getByRole("searchbox", { name: "Search courses" });
  await search.fill("Closed-Loop");
  const catalogLink = page.getByRole("link", {
    name: courseTitle,
    exact: true,
  });
  await expect(catalogLink).toBeVisible();
  await catalogLink.click();
  await expect(
    page.locator(".section-heading").getByRole("heading", {
      name: courseTitle,
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByText("8 available lessons", { exact: true }),
  ).toBeVisible();

  await page.goto("/");
  const pathway = page
    .locator("details.pathway-card")
    .filter({ has: page.getByText(pathwayTitle, { exact: true }) });
  await expect(pathway).toHaveCount(1);
  const pathwaySummary = pathway.locator("summary");
  await pathwaySummary.focus();
  await page.keyboard.press("Enter");
  await expect(pathway).toHaveAttribute("open", "");
  const pathwayLink = pathway.getByRole("link", {
    name: `Open available partial package: ${courseTitle}`,
    exact: true,
  });
  await expect(pathwayLink).toHaveAttribute("href", `#/course/${courseId}`);
  await expectBasicAccessibility(page);
  await pathwayLink.click();

  const lessonNavigation = page.getByRole("navigation", {
    name: "Lessons",
    exact: true,
  });
  for (const [index, lesson] of lessons.entries()) {
    await lessonNavigation
      .getByRole("link", { name: lesson.title, exact: true })
      .click();
    await expect(page).toHaveURL(
      new RegExp(`#\\/course\\/${courseId}\\/lesson\\/${lesson.id}$`),
    );
    const article = page.locator("article.lesson-reader");
    await expect(
      article.getByRole("heading", {
        name: lesson.title,
        exact: true,
        level: 2,
      }),
    ).toBeVisible();
    await expect(article).toContainText(lesson.evidence);
    await expect(page.locator("[data-question-id]")).toHaveCount(6);
    const retrieval = page.getByRole("region", {
      name: "Retrieval practice",
      exact: true,
    });
    await expect(
      retrieval.getByText("Reveal answer", { exact: true }),
    ).toHaveCount(3);
    const submit = page.getByRole("button", {
      name: "Submit practice response",
      exact: true,
    });
    await expect(submit).toHaveCount(6);
    await expect(submit.first()).toBeDisabled();

    if (index === 1) {
      const practice = page.locator(
        `[data-question-id="${courseId}-2:dli-from-ppfd"]`,
      );
      await expect(practice).toContainText(
        "A synthetic canopy measurement is PPFD 200",
      );
      await expect(practice.locator('input[name="value"]')).toBeVisible();
      const firstCard = retrieval.locator("details").first();
      await firstCard.locator("summary").focus();
      await page.keyboard.press("Enter");
      await expect(firstCard).toHaveAttribute("open", "");
      await expectBasicAccessibility(page);
    }

    for (const resource of lesson.resources ?? []) {
      const csv = article.locator(
        `a[href="/api/v1/courses/${courseId}/resources/${resource}"]`,
      );
      await expect(csv).toBeVisible();
      const response = await page.request.get(
        `/api/v1/courses/${courseId}/resources/${resource}`,
      );
      expect(response.ok()).toBeTruthy();
      expect(response.headers()["content-type"]).toContain("text/csv");
      expect(await response.body()).toEqual(
        await readFile(
          new URL(
            `../../content/courses/${courseId}/${resource}`,
            import.meta.url,
          ),
        ),
      );
      expect(await response.text()).toContain("synthetic-original");
    }
  }

  await page.goto(`/#/course/${courseId}/cases`);
  const cases = page.getByRole("region", {
    name: "Case response",
    exact: true,
  });
  await expect(cases).toHaveCount(6);
  await expect(cases.first()).toContainText(
    "A synthetic proposal claims to be a closed-loop habitat",
  );
  await expect(cases.first()).toContainText("zero-point self-check");
  await expect(cases.first().getByRole("checkbox")).toHaveCount(6);
  await expect(
    cases.first().getByRole("textbox", { name: "Your response" }),
  ).toBeDisabled();
  await expect(cases.first().getByRole("checkbox").first()).toBeDisabled();
  await expect(
    page.getByRole("button", { name: "Save draft", exact: true }),
  ).toHaveCount(0);
  await expectBasicAccessibility(page);
  expect(writes).toEqual([]);
});

test("habitat ledger defaults, recovery boundaries, invalid inputs and keyboard calculation work", async ({
  page,
}) => {
  const writes = monitorApiWrites(page);
  await page.goto("/#/tools/habitat-ledger");
  await expect(
    page.getByRole("heading", { name: "Habitat ledger", exact: true }),
  ).toBeVisible();
  const expectedDefaults = [
    ["PPFD (μmol/m²/s)", "200"],
    ["Photoperiod (h/day)", "16"],
    ["Lighting power (W)", "120"],
    ["Other continuous equipment (W)", "80"],
    ["Water demand (L/day)", "40"],
    ["Recovered water (L/day)", "30"],
    ["Reservoir volume (L)", "120"],
  ] as const;
  for (const [name, value] of expectedDefaults)
    await expect(page.getByRole("spinbutton", { name })).toHaveValue(value);

  const calculate = page.getByRole("button", {
    name: "Calculate",
    exact: true,
  });
  const reset = page.getByRole("button", {
    name: "Reset example",
    exact: true,
  });
  const status = page.getByRole("status");
  await calculate.focus();
  await page.keyboard.press("Enter");
  for (const value of [
    "11.52 mol/m²/day",
    "1.92 kWh/day",
    "3.84 kWh/day",
    "10 L/day",
    "75 %",
    "12 days",
  ])
    await expect(status.getByText(value, { exact: true })).toBeVisible();
  for (const [name, id] of [
    [courseTitle, courseId],
    ["Biochemistry I: Proteins, Enzymes & Metabolism", "biochemistry"],
    ["Electrical Circuits & Instrumentation", "circuits"],
  ])
    await expect(page.getByRole("link", { name, exact: true })).toHaveAttribute(
      "href",
      `#/course/${id}`,
    );
  await expect(page.getByText(/Daily accounting only/)).toContainText(
    "not crop yield, HVAC, nutrient prescription, or life-support certification",
  );

  const ppfd = page.getByRole("spinbutton", { name: "PPFD (μmol/m²/s)" });
  await ppfd.fill("400");
  await calculate.click();
  await expect(
    status.getByText("23.04 mol/m²/day", { exact: true }),
  ).toBeVisible();
  await reset.click();
  await expect(ppfd).toHaveValue("200");
  await expect(status.locator(".tool-results")).toHaveCount(0);

  const recovered = page.getByRole("spinbutton", {
    name: "Recovered water (L/day)",
  });
  await recovered.fill("40");
  await calculate.click();
  await expect(status.getByText("100 %", { exact: true })).toBeVisible();
  await expect(
    status.getByText("Reservoir endurance", { exact: true }),
  ).toHaveCount(0);

  await recovered.fill("41");
  await calculate.click();
  await expect(page.getByRole("alert")).toContainText(
    "Recovered water cannot exceed water demand",
  );
  await reset.click();
  await ppfd.fill("-1");
  await calculate.click();
  await expect(page.getByRole("alert")).toContainText("must be at least 0");
  await reset.click();
  await ppfd.fill("");
  await calculate.click();
  await expect(page.getByRole("alert")).toContainText("finite number");
  await reset.click();
  await page
    .getByRole("spinbutton", { name: "Photoperiod (h/day)" })
    .fill("25");
  await calculate.click();
  await expect(page.getByRole("alert")).toContainText("must be at most 24");
  await reset.click();
  await ppfd.fill("1e308");
  await page
    .getByRole("spinbutton", { name: "Photoperiod (h/day)" })
    .fill("24");
  await calculate.click();
  await expect(page.getByRole("alert")).toContainText("numeric range");

  await reset.click();
  for (const name of [
    "PPFD (μmol/m²/s)",
    "Lighting power (W)",
    "Other continuous equipment (W)",
  ])
    await page.getByRole("spinbutton", { name }).fill("0");
  await calculate.click();
  for (const value of ["0 mol/m²/day", "0 kWh/day"])
    await expect(
      status.getByText(value, { exact: true }).first(),
    ).toBeVisible();
  await reset.click();
  await calculate.click();
  await expectBasicAccessibility(page);
  expect(writes).toEqual([]);
});

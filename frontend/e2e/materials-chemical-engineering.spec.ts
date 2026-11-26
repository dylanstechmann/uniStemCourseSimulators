import AxeBuilder from "@axe-core/playwright";
import { expect, test, type Page } from "@playwright/test";
import { readFileSync } from "node:fs";

const fixtures = [
  {
    id: "materials-science",
    search: "Materials Science",
    pathway: "Science and Mathematics Foundation",
  },
  {
    id: "chemical-engineering-foundations",
    search: "Chemical Engineering Foundations",
    pathway: "Chemical Process Engineering",
  },
  {
    id: "materials-engineering-fabrication",
    search: "Materials Engineering for Fabrication",
    pathway: "Mechanical Engineering and Robotics",
  },
  {
    id: "chemical-process-design-scale-up",
    search: "Chemical Process Design & Scale-Up",
    pathway: "Chemical Process Engineering",
  },
] as const;

type Lesson = {
  id: string;
  title: string;
  worked_example: string;
};
type Manifest = {
  title: string;
  learner_resources: string[];
  modules: { lessons: Lesson[] }[];
};
type CaseFile = { cases: { prompt: string }[] };

function packageUrl(courseId: string, path: string) {
  return new URL(`../../content/courses/${courseId}/${path}`, import.meta.url);
}

const courses = fixtures.map((fixture) => {
  const manifest = JSON.parse(
    readFileSync(packageUrl(fixture.id, "course.json"), "utf8"),
  ) as Manifest;
  const cases = JSON.parse(
    readFileSync(packageUrl(fixture.id, "rubrics/case-studio.json"), "utf8"),
  ) as CaseFile;
  return {
    ...fixture,
    ...manifest,
    lessons: manifest.modules.flatMap((module) => module.lessons),
    cases: cases.cases,
  };
});

function monitorApiWrites(page: Page) {
  const writes: string[] = [];
  page.on("request", (request) => {
    if (
      request.url().includes("/api/") &&
      !["GET", "HEAD", "OPTIONS"].includes(request.method())
    )
      writes.push(`${request.method()} ${request.url()}`);
  });
  return writes;
}

async function expectBasicAccessibility(page: Page) {
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);
}

async function calculateWithKeyboard(page: Page) {
  await page.getByRole("button", { name: "Calculate", exact: true }).focus();
  await page.keyboard.press("Enter");
}

test("four engineering packages expose every route, item, card, case and synthetic CSV without writes", async ({
  page,
}) => {
  test.setTimeout(300_000);
  const writes = monitorApiWrites(page);
  for (const [courseIndex, course] of courses.entries()) {
    expect(course.lessons).toHaveLength(8);
    expect(course.learner_resources).toHaveLength(2);
    expect(course.cases).toHaveLength(6);

    await page.goto("/");
    await page
      .getByRole("searchbox", { name: "Search courses" })
      .fill(course.search);
    const catalogLink = page.getByRole("link", {
      name: course.title,
      exact: true,
    });
    await expect(catalogLink).toBeVisible();
    await catalogLink.click();
    await expect(
      page.locator(".section-heading").getByRole("heading", {
        name: course.title,
        exact: true,
      }),
    ).toBeVisible();
    await expect(
      page.getByText("8 available lessons", { exact: true }),
    ).toBeVisible();

    await page.goto("/");
    const pathway = page
      .locator("details.pathway-card")
      .filter({ has: page.getByText(course.pathway, { exact: true }) });
    await expect(pathway).toHaveCount(1);
    await pathway.locator("summary").focus();
    await page.keyboard.press("Enter");
    await expect(pathway).toHaveAttribute("open", "");
    const pathwayLink = pathway.getByRole("link", {
      name: `Open available partial package: ${course.title}`,
      exact: true,
    });
    await expect(pathwayLink).toHaveAttribute("href", `#/course/${course.id}`);
    if (courseIndex === 0) await expectBasicAccessibility(page);
    await pathwayLink.click();

    const lessonNavigation = page.getByRole("navigation", {
      name: "Lessons",
      exact: true,
    });
    for (const [lessonIndex, lesson] of course.lessons.entries()) {
      await lessonNavigation
        .getByRole("link", { name: lesson.title, exact: true })
        .click();
      await expect(page).toHaveURL(
        new RegExp(`#/course/${course.id}/lesson/${lesson.id}$`),
      );
      const article = page.locator("article.lesson-reader");
      await expect(
        article.getByRole("heading", {
          name: lesson.title,
          exact: true,
          level: 2,
        }),
      ).toBeVisible();
      await expect(article.locator(".worked-example")).toContainText(
        lesson.worked_example,
      );
      await expect(page.locator("[data-question-id]")).toHaveCount(6);
      const submit = page.getByRole("button", {
        name: "Submit practice response",
        exact: true,
      });
      await expect(submit).toHaveCount(6);
      for (let index = 0; index < 6; index += 1)
        await expect(submit.nth(index)).toBeDisabled();
      await expect(
        article.getByRole("button", { name: "Mark as read", exact: true }),
      ).toBeDisabled();
      const retrieval = page.getByRole("region", {
        name: "Retrieval practice",
        exact: true,
      });
      await expect(
        retrieval.getByText("Reveal answer", { exact: true }),
      ).toHaveCount(3);

      if (courseIndex === 0 && lessonIndex === 1) {
        const firstCard = retrieval.locator("details").first();
        await firstCard.locator("summary").focus();
        await page.keyboard.press("Enter");
        await expect(firstCard).toHaveAttribute("open", "");
        await expectBasicAccessibility(page);
      }

      const resourceIndex =
        lessonIndex === 6 ? 0 : lessonIndex === 7 ? 1 : null;
      if (resourceIndex !== null) {
        const resource = course.learner_resources[resourceIndex];
        await expect(
          article.locator(
            `a[href="/api/v1/courses/${course.id}/resources/${resource}"]`,
          ),
        ).toBeVisible();
      }
    }

    for (const resource of course.learner_resources) {
      const response = await page.request.get(
        `/api/v1/courses/${course.id}/resources/${resource}`,
      );
      expect(response.ok()).toBeTruthy();
      expect(response.headers()["content-type"]).toContain("text/csv");
      expect(await response.body()).toEqual(
        readFileSync(packageUrl(course.id, resource)),
      );
      expect(await response.text()).toContain("synthetic-original");
    }

    await page.goto(`/#/course/${course.id}/cases`);
    const caseEditors = page.getByRole("region", {
      name: "Case response",
      exact: true,
    });
    await expect(caseEditors).toHaveCount(6);
    await expect(caseEditors.first()).toContainText(course.cases[0].prompt);
    for (let index = 0; index < 6; index += 1) {
      const editor = caseEditors.nth(index);
      await expect(
        editor.getByRole("textbox", { name: "Your response" }),
      ).toBeDisabled();
      await expect(editor.getByRole("checkbox").first()).toBeDisabled();
    }
    await expect(
      page.getByRole("button", { name: "Save draft", exact: true }),
    ).toHaveCount(0);
    if (courseIndex === 0) await expectBasicAccessibility(page);
  }
  expect(writes).toEqual([]);
});

test("four engineering calculators cover defaults, valid and boundary states, validation, reset, links and accessibility", async ({
  page,
}) => {
  test.setTimeout(180_000);
  const writes = monitorApiWrites(page);
  const status = page.getByRole("status");
  const reset = page.getByRole("button", {
    name: "Reset example",
    exact: true,
  });

  await page.goto("/#/tools/crystal-diffraction");
  for (const [name, value] of [
    ["Cubic lattice parameter a (nm)", "0.4"],
    ["Miller index h", "1"],
    ["Miller index k", "0"],
    ["Miller index l", "0"],
    ["Wavelength λ (nm)", "0.154"],
  ])
    await expect(page.getByRole("spinbutton", { name })).toHaveValue(value);
  await calculateWithKeyboard(page);
  for (const value of ["0.4 nm", "11.0987 °", "22.1974 °"])
    await expect(status.getByText(value, { exact: true })).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Materials Science", exact: true }),
  ).toHaveAttribute("href", "#/course/materials-science");
  await expectBasicAccessibility(page);
  const wavelength = page.getByRole("spinbutton", {
    name: "Wavelength λ (nm)",
  });
  await wavelength.fill("0.8");
  await calculateWithKeyboard(page);
  await expect(status.getByText("90 °", { exact: true })).toBeVisible();
  await expect(status.getByText("180 °", { exact: true })).toBeVisible();
  await wavelength.fill("0.81");
  await calculateWithKeyboard(page);
  await expect(page.getByRole("alert")).toContainText("cannot exceed 2d");
  await reset.click();
  for (const name of ["Miller index h", "Miller index k", "Miller index l"])
    await page.getByRole("spinbutton", { name }).fill("0");
  await calculateWithKeyboard(page);
  await expect(page.getByRole("alert")).toContainText("cannot all be zero");

  await page.goto("/#/tools/stream-balance");
  await calculateWithKeyboard(page);
  for (const value of [
    "80 mol/h",
    "40 mol/h",
    "36 mol/h",
    "4 mol/h",
    "0 mol/h",
  ])
    await expect(
      status.getByText(value, { exact: true }).first(),
    ).toBeVisible();
  await expect(
    status.getByText("B unrecovered", { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: "Chemical Engineering Foundations",
      exact: true,
    }),
  ).toHaveAttribute("href", "#/course/chemical-engineering-foundations");
  await expectBasicAccessibility(page);
  const feed = page.getByRole("spinbutton", {
    name: "Total feed flow (mol/h)",
  });
  await feed.fill("0");
  await calculateWithKeyboard(page);
  await expect(status.getByText("0 mol/h", { exact: true })).toHaveCount(6);
  await feed.fill("");
  await calculateWithKeyboard(page);
  await expect(page.getByRole("alert")).toContainText("finite number");
  await reset.click();
  await page
    .getByRole("spinbutton", { name: "A conversion fraction" })
    .fill("1.1");
  await calculateWithKeyboard(page);
  await expect(page.getByRole("alert")).toContainText("at most 1");

  await page.goto("/#/tools/tolerance-stack");
  await calculateWithKeyboard(page);
  await expect(status.getByText("60 mm", { exact: true })).toBeVisible();
  await expect(status.getByText("0.6 mm", { exact: true })).toBeVisible();
  await expect(status.getByText(/Conditional independent RSS/)).toHaveCount(0);
  await expect(status).toContainText(
    "independent variation has not been declared",
  );
  const model = page.getByRole("combobox", { name: "RSS variation model" });
  await model.selectOption("independent");
  await calculateWithKeyboard(page);
  await expect(status.getByText("0.374166 mm", { exact: true })).toBeVisible();
  await expect(status).toContainText(
    "conditional on the declared independent-variation model",
  );
  await expect(
    page.getByRole("link", {
      name: "Materials Engineering for Fabrication",
      exact: true,
    }),
  ).toHaveAttribute("href", "#/course/materials-engineering-fabrication");
  await expectBasicAccessibility(page);
  await reset.click();
  await expect(model).toHaveValue("not-declared");
  await page
    .getByRole("spinbutton", { name: "Symmetric tolerance 1 (±mm)" })
    .fill("-0.1");
  await calculateWithKeyboard(page);
  await expect(page.getByRole("alert")).toContainText("at least 0");

  await page.goto("/#/tools/process-capability");
  const state = page.getByRole("combobox", { name: "Declared process state" });
  await calculateWithKeyboard(page);
  await expect(status.getByText("Cp (declared stable process)")).toHaveCount(0);
  await expect(status).toContainText("process stability is unknown");
  await state.selectOption("unstable");
  await calculateWithKeyboard(page);
  await expect(status.getByText("Cpk (declared stable process)")).toHaveCount(
    0,
  );
  await expect(status).toContainText("declared unstable");
  await state.selectOption("stable");
  await calculateWithKeyboard(page);
  await expect(status.getByText("1.66667", { exact: true })).toHaveCount(2);
  for (const [name, id] of [
    [
      "Materials Engineering for Fabrication",
      "materials-engineering-fabrication",
    ],
    ["Chemical Process Design & Scale-Up", "chemical-process-design-scale-up"],
  ])
    await expect(page.getByRole("link", { name, exact: true })).toHaveAttribute(
      "href",
      `#/course/${id}`,
    );
  await expectBasicAccessibility(page);
  await page
    .getByRole("spinbutton", { name: "Sample standard deviation s" })
    .fill("0");
  await calculateWithKeyboard(page);
  await expect(page.getByRole("alert")).toContainText("greater than 0");
  await reset.click();
  await page
    .getByRole("spinbutton", { name: "Lower specification limit (LSL)" })
    .fill("60");
  await calculateWithKeyboard(page);
  await expect(page.getByRole("alert")).toContainText("less than USL");
  await reset.click();
  await expect(state).toHaveValue("unknown");
  expect(writes).toEqual([]);
});

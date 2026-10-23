import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("public case studios expose authored science and engineering checklists", async ({
  page,
}) => {
  // Each course lists its preserved case first, followed by project milestones.
  const caseCounts: Record<string, number> = {
    "cell-biology": 6,
    circuits: 6,
    biochemistry: 6,
  };
  for (const course of ["cell-biology", "circuits", "biochemistry"]) {
    await page.goto(`/#/course/${course}/cases`);
    await expect(
      page.getByRole("heading", { name: "Case studio", exact: true }),
    ).toBeVisible();
    const cases = page.getByRole("region", {
      name: "Case response",
      exact: true,
    });
    await expect(cases).toHaveCount(caseCounts[course]);
    const firstCase = cases.first();
    await expect(
      firstCase.getByRole("heading", { name: "Case prompt", exact: true }),
    ).toBeVisible();
    const limitations = page.locator(
      'aside[aria-label="Course limitations"] details',
    );
    await page.getByText(/Read all .* course limitations/).click();
    await expect(limitations).toHaveAttribute("open", "");
    await page.getByText(/Read all .* course limitations/).click();
    for (const response of await page
      .getByRole("textbox", { name: "Your response" })
      .all()) {
      await expect(response).toBeDisabled();
    }
    await expect(firstCase.getByRole("checkbox")).toHaveCount(
      course === "biochemistry" ? 6 : 3,
    );
    await expect(
      page.getByRole("link", { name: "Case studio", exact: true }),
    ).toHaveAttribute("aria-current", "page");
    expect(
      (
        await new AxeBuilder({ page })
          .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
          .analyze()
      ).violations,
    ).toEqual([]);
  }
});

test("learner drafts survive reload and protect against stale browser edits", async ({
  page,
  context,
}) => {
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByText(
      "Guest session started. You can now enroll and save your work.",
    ),
  ).toBeVisible();
  await page.goto("/#/course/cell-biology/cases");
  await page
    .getByRole("button", { name: "Enroll in partial course", exact: true })
    .click();
  // The preserved case comes first; the project milestone self-checks follow it.
  const firstCase = page
    .getByRole("region", { name: "Case response", exact: true })
    .first();
  const response = firstCase.getByRole("textbox", { name: "Your response" });
  await expect(response).toBeEnabled();
  const text =
    "Compare matched surface abundance with transport in mutant, wild type, and a negative control. Test membrane potential and viability before attributing the loss to the pore.";
  await response.fill(text);
  await firstCase.getByRole("checkbox").first().focus();
  await page.keyboard.press("Space");
  await firstCase
    .getByRole("button", { name: "Save draft", exact: true })
    .focus();
  await page.keyboard.press("Enter");
  await expect(
    firstCase.getByRole("status").filter({ hasText: "Draft saved" }),
  ).toBeVisible();
  await page.reload();
  await expect(response).toHaveValue(text);
  await expect(firstCase.getByRole("checkbox").first()).toBeChecked();

  const otherTab = await context.newPage();
  await otherTab.goto("/#/course/cell-biology/cases");
  const otherCase = otherTab
    .getByRole("region", { name: "Case response", exact: true })
    .first();
  await expect(
    otherCase.getByRole("textbox", { name: "Your response" }),
  ).toHaveValue(text);
  await response.fill("A newer saved response from the first tab.");
  await firstCase
    .getByRole("button", { name: "Save draft", exact: true })
    .click();
  await expect(firstCase.getByText(/revision 2/)).toBeVisible();
  await otherCase
    .getByRole("textbox", { name: "Your response" })
    .fill("Unsaved text from the stale tab.");
  await otherCase
    .getByRole("button", { name: "Save draft", exact: true })
    .click();
  await expect(otherCase.getByRole("alert")).toContainText(
    "saved draft changed",
  );
  await expect(otherCase.getByRole("textbox")).toHaveValue(
    "Unsaved text from the stale tab.",
  );
  await otherCase
    .getByRole("button", { name: "Replace editor with saved draft" })
    .click();
  await expect(otherCase.getByRole("textbox")).toHaveValue(
    "A newer saved response from the first tab.",
  );
  await otherTab.close();

  const exported = await (
    await page.request.get("/api/v1/learner/export")
  ).json();
  expect(exported.case_drafts).toHaveLength(1);
  expect(exported.case_drafts[0].revision).toBe(2);
  expect(exported.attempts).toEqual([]);
  const accessibility = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  expect(accessibility.violations).toEqual([]);
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.screenshot({
    path: "test-results/case-studio-desktop.png",
    fullPage: true,
  });

  const course = await (
    await page.request.get("/api/v1/courses/cell-biology")
  ).json();
  await page.goto(
    `/#/course/cell-biology/version/${encodeURIComponent(course.version)}`,
  );
  await page.getByRole("link", { name: "Read archived case studio" }).click();
  const archivedCase = page
    .getByRole("region", { name: "Case response", exact: true })
    .first();
  await expect(
    archivedCase.getByRole("textbox", { name: "Your response" }),
  ).toHaveValue("A newer saved response from the first tab.");
  await expect(
    archivedCase.getByRole("textbox", { name: "Your response" }),
  ).toBeDisabled();
  await expect(
    archivedCase.getByText(
      /archived case and its saved response are read-only/,
    ),
  ).toBeVisible();
});

test("case prompt and checklist fit a narrow screen", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/#/course/circuits/cases");
  await expect(
    page.getByRole("region", { name: "Case response", exact: true }),
  ).toHaveCount(6);
  await expect(
    page.getByRole("heading", { name: "Case prompt", exact: true }).first(),
  ).toBeVisible();
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= window.innerWidth,
    ),
  ).toBe(true);
  await page.screenshot({
    path: "test-results/case-studio-mobile.png",
    fullPage: true,
  });
});

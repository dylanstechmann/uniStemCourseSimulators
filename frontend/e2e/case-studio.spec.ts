import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("public case studios expose authored science and engineering checklists", async ({
  page,
}) => {
  for (const course of ["cell-biology", "circuits", "biochemistry"]) {
    await page.goto(`/#/course/${course}/cases`);
    await expect(
      page.getByRole("heading", { name: "Case studio", exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: "Case prompt", exact: true }),
    ).toBeVisible();
    const limitations = page.locator(
      'aside[aria-label="Course limitations"] details',
    );
    await page.getByText(/Read all .* course limitations/).click();
    await expect(limitations).toHaveAttribute("open", "");
    await page.getByText(/Read all .* course limitations/).click();
    await expect(
      page.getByRole("textbox", { name: "Your response" }),
    ).toBeDisabled();
    await expect(page.getByRole("checkbox")).toHaveCount(
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
  const response = page.getByRole("textbox", { name: "Your response" });
  await expect(response).toBeEnabled();
  const text =
    "Compare matched surface abundance with transport in mutant, wild type, and a negative control. Test membrane potential and viability before attributing the loss to the pore.";
  await response.fill(text);
  await page.getByRole("checkbox").first().focus();
  await page.keyboard.press("Space");
  await page.getByRole("button", { name: "Save draft", exact: true }).focus();
  await page.keyboard.press("Enter");
  await expect(
    page.getByRole("status").filter({ hasText: "Draft saved" }),
  ).toBeVisible();
  await page.reload();
  await expect(response).toHaveValue(text);
  await expect(page.getByRole("checkbox").first()).toBeChecked();

  const otherTab = await context.newPage();
  await otherTab.goto("/#/course/cell-biology/cases");
  await expect(
    otherTab.getByRole("textbox", { name: "Your response" }),
  ).toHaveValue(text);
  await response.fill("A newer saved response from the first tab.");
  await page.getByRole("button", { name: "Save draft", exact: true }).click();
  await expect(page.getByText(/revision 2/)).toBeVisible();
  await otherTab
    .getByRole("textbox", { name: "Your response" })
    .fill("Unsaved text from the stale tab.");
  await otherTab
    .getByRole("button", { name: "Save draft", exact: true })
    .click();
  await expect(otherTab.getByRole("alert")).toContainText(
    "saved draft changed",
  );
  await expect(otherTab.getByRole("textbox")).toHaveValue(
    "Unsaved text from the stale tab.",
  );
  await otherTab
    .getByRole("button", { name: "Replace editor with saved draft" })
    .click();
  await expect(otherTab.getByRole("textbox")).toHaveValue(
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
  await expect(
    page.getByRole("textbox", { name: "Your response" }),
  ).toHaveValue("A newer saved response from the first tab.");
  await expect(
    page.getByRole("textbox", { name: "Your response" }),
  ).toBeDisabled();
  await expect(
    page.getByText(/archived case and its saved response are read-only/),
  ).toBeVisible();
});

test("case prompt and checklist fit a narrow screen", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/#/course/circuits/cases");
  await expect(
    page.getByRole("heading", { name: "Case prompt", exact: true }),
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

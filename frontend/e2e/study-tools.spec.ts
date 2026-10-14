import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("public scientific calculators work with keyboard input and accessible results", async ({
  page,
}) => {
  const writes: string[] = [];
  page.on("request", (request) => {
    if (
      request.url().includes("/api/") &&
      !["GET", "HEAD", "OPTIONS"].includes(request.method())
    )
      writes.push(request.url());
  });
  await page.goto("/#/tools/dilution");
  await expect(
    page.getByRole("heading", { name: "Study tools", exact: true }),
  ).toBeVisible();
  const calculators = page.getByRole("navigation", {
    name: "Scientific calculators",
  });
  const examples = [
    { name: "Dilution", result: "0.5 mL" },
    { name: "Buffer pH", result: "8.2" },
    { name: "Enzyme kinetics", result: "66.6667 μM/min" },
    { name: "RC charging", result: "1 s" },
    { name: "Diffusion timescale", result: "10 s" },
    { name: "Ohm’s law", result: "0.5 mA" },
  ];
  for (const example of examples) {
    const link = calculators.getByRole("link", {
      name: example.name,
      exact: true,
    });
    await link.focus();
    await page.keyboard.press("Enter");
    await expect(
      page.getByRole("heading", { name: example.name, exact: true }),
    ).toBeVisible();
    await expect(link).toHaveAttribute("aria-current", "page");
    await page.getByRole("button", { name: "Calculate", exact: true }).focus();
    await page.keyboard.press("Enter");
    await expect(
      page.getByRole("status").getByText(example.result, { exact: true }),
    ).toBeVisible();
    const accessibility = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .analyze();
    expect(accessibility.violations).toEqual([]);
  }
  await calculators
    .getByRole("link", { name: "Dilution", exact: true })
    .click();
  await page
    .getByRole("spinbutton", { name: "Target concentration (mM)" })
    .fill("101");
  await page.getByRole("button", { name: "Calculate", exact: true }).click();
  await expect(page.getByRole("alert")).toContainText("cannot exceed");
  expect(writes).toEqual([]);
});

test("calculator navigation and results fit a narrow screen", async ({
  page,
}) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/#/tools/rc");
  await expect(
    page.getByRole("heading", { name: "RC charging", exact: true }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Calculate", exact: true }).click();
  await expect(page.getByText("63.2121 %", { exact: true })).toBeVisible();
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= window.innerWidth,
    ),
  ).toBe(true);
});

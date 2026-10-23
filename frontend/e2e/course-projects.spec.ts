import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";
import { readFile } from "node:fs/promises";

// Values are independently recomputed in test_remaining_course_project_routes.py.
// The browser verifies rendering, precision handling, submission and persistence.
const plans = [
  {
    course: "circuits",
    title: "Sensor-channel budget project guide (optional, ungraded)",
    numeric: {
      loading: "0.990",
      low: "1.36",
      high: "2.64",
    },
    choices: {
      basis: "1",
    },
    points: 4,
  },
  {
    course: "physiology",
    title: "Renal-clearance ledger project guide (optional, ungraded)",
    numeric: {
      gfr: "72.0",
      reference_rate: "36.0",
    },
    choices: {
      assumption: "1",
    },
    points: 3,
  },
  {
    course: "signals-control",
    title: "Sampled-loop portfolio project guide (optional, ungraded)",
    numeric: {
      sample_frequency: "5.00",
      nyquist: "2.50",
      alias: "1.00",
    },
    choices: {
      digital: "2",
    },
    points: 4,
  },
  {
    course: "general-chemistry-1",
    title: "Gas-equilibrium ledger project guide (optional, ungraded)",
    numeric: {
      extent_max: "2.00",
      conserved: "4.00",
    },
    choices: {
      reverse: "1",
    },
    points: 3,
  },
  {
    course: "organic-chemistry",
    title: "Aldol-identity dossier project guide (optional, ungraded)",
    numeric: {},
    choices: {
      donor: "1",
      acceptor: "2",
      oxygen: "0",
    },
    points: 3,
  },
  {
    course: "statistics",
    title: "Confirmatory-protocol dossier project guide (optional, ungraded)",
    numeric: {
      units: "16",
      observations: "64",
    },
    choices: {
      analysis_unit: "1",
    },
    points: 3,
  },
  {
    course: "robotics",
    title: "Trajectory-margin portfolio project guide (optional, ungraded)",
    numeric: {
      speed: "0.900",
      acceleration: "3.60",
    },
    choices: {
      endpoints: "2",
    },
    points: 3,
  },
  {
    course: "geroscience",
    title: "Surrogate-evidence dossier project guide (optional, ungraded)",
    numeric: {
      marker_width: "2.00",
      function_width: "1.20",
    },
    choices: {
      nulls: "1",
      precision: "2",
    },
    points: 4,
  },
];

for (const plan of plans) {
  test(`${plan.course}: project reading, rehearsal and private milestone work end to end`, async ({
    page,
  }) => {
    await page.goto("/#/account");
    await page
      .getByRole("button", { name: "Start guest session", exact: true })
      .click();
    await expect(
      page.getByRole("heading", { name: "Guest session", exact: true }),
    ).toBeVisible();
    try {
      await page.goto(`/#/course/${plan.course}`);
      await page
        .getByRole("button", { name: "Enroll in partial course", exact: true })
        .click();
      await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
      await page
        .getByRole("navigation", { name: "Lessons", exact: true })
        .getByRole("link", { name: plan.title, exact: true })
        .click();
      await expect(
        page.getByRole("heading", { name: plan.title, exact: true }),
      ).toBeVisible();
      await expect(
        page.getByRole("heading", {
          name: "Worked example: a separate case",
          exact: true,
        }),
      ).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(5);
      await expect(
        page
          .getByRole("region", { name: "Retrieval practice", exact: true })
          .getByText("Reveal answer", { exact: true }),
      ).toHaveCount(5);
      const csv = page
        .locator(
          '.lesson-reader a[href*="/resources/"][href$="-rehearsal.csv"]',
        )
        .first();
      await expect(csv).toBeVisible();
      const href = await csv.getAttribute("href");
      expect(href).toContain(
        `/api/v1/courses/${plan.course}/resources/assignments/`,
      );
      const resource = await page.request.get(href!);
      expect(resource.ok()).toBeTruthy();
      expect(resource.headers()["content-type"]).toContain("text/csv");
      const relative = href!.split("/resources/")[1];
      expect(await resource.body()).toEqual(
        await readFile(
          new URL(
            `../../content/courses/${plan.course}/${relative}`,
            import.meta.url,
          ),
        ),
      );
      const question = page.locator(
        `[data-question-id="${plan.course}-project:rehearsal-1"]`,
      );
      for (const [field, value] of Object.entries(plan.numeric)) {
        await question.locator(`input[name="${field}"]`).fill(value);
      }
      for (const [field, value] of Object.entries(plan.choices)) {
        await question.locator(`select[name="${field}"]`).selectOption(value);
      }
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${plan.points} / ${plan.points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
      await page
        .getByRole("link", { name: "Case studio", exact: true })
        .click();
      const cases = page.getByRole("region", {
        name: "Case response",
        exact: true,
      });
      await expect(cases).toHaveCount(6);
      const milestone = cases.nth(1);
      const response = `${plan.course}: my model, calculation, evidence and remaining limits.`;
      await milestone
        .getByRole("textbox", { name: "Your response" })
        .fill(response);
      await milestone.getByRole("checkbox").first().check();
      await milestone
        .getByRole("button", { name: "Save draft", exact: true })
        .click();
      await expect(milestone.getByRole("status")).toContainText("Draft saved");
      await page.reload();
      await expect(
        milestone.getByRole("textbox", { name: "Your response" }),
      ).toHaveValue(response);
      await expect(milestone.getByRole("checkbox").first()).toBeChecked();
      const exported = await (
        await page.request.get("/api/v1/learner/export")
      ).json();
      expect(exported.case_drafts).toHaveLength(1);
      expect(exported.case_drafts[0].case_id).toBe(`${plan.course}:project-m1`);
      expect(exported.attempts).toHaveLength(1);
      expect(exported.graded_submissions).toEqual([]);
    } finally {
      const status = await page.evaluate(async () => {
        const session = await (await fetch("/api/v1/auth/session")).json();
        if (!session.user) return null;
        return (
          await fetch("/api/v1/learner", {
            method: "DELETE",
            headers: { "X-CSRF-Token": session.csrf_token },
          })
        ).status;
      });
      if (status !== null) expect(status).toBe(204);
    }
  });
}

test("programming semester foundations and all five implementation packets deliver and grade", async ({
  page,
}) => {
  test.setTimeout(120_000);
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: { forward: "3.64", central: "3.04" },
      choices: { order: "1" },
    },
    {
      number: 17,
      numeric: { mean: "3.00", variance: "2.50", se: "0.707" },
      choices: {},
    },
    {
      number: 18,
      numeric: { multiplier: "0.500", x1: "1.00", x2: "2.00" },
      choices: {},
    },
    {
      number: 19,
      numeric: { first: "17.0", second: "8.00", ratio: "0.600" },
      choices: {},
    },
    {
      number: 20,
      numeric: { dx: "0.167", dy: "1.17", residual: "1.39" },
      choices: {},
    },
    {
      number: 21,
      numeric: { euler: "1.40", heun: "1.49", backward: "1.54" },
      choices: {},
    },
    {
      number: 22,
      numeric: { accepted: "4", excluded: "4", specimens: "2" },
      choices: {},
    },
    {
      number: 23,
      numeric: { value: "1.31", integral: "1.83" },
      choices: { truth: "2" },
    },
    {
      number: 24,
      numeric: { mean: "0.333", probability: "0.200" },
      choices: { dependence: "0" },
    },
    {
      number: 25,
      numeric: { center: "2.00" },
      choices: { ends: "0", evidence: "2" },
    },
    {
      number: 26,
      numeric: { a: "0.368", b: "0.233", c: "0.400" },
      choices: { balance: "0" },
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/programming");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/programming/lesson/programming-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 22 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="programming-${check.number}:method-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
      if (check.number === 22) {
        const href = await page
          .getByRole("link", { name: "observation table", exact: true })
          .getAttribute("href");
        expect(href).toBe(
          "/api/v1/courses/programming/resources/assignments/semester-observations.csv",
        );
        const data = await page.request.get(href!);
        expect(await data.body()).toEqual(
          await readFile(
            new URL(
              "../../content/courses/programming/assignments/semester-observations.csv",
              import.meta.url,
            ),
          ),
        );
      }
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(11);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("transport semester foundations and connected assignments deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 17,
      numeric: { alpha: "2.00", beta: "6.00", beta_amount: "6.00e-3" },
      choices: {},
    },
    {
      number: 18,
      numeric: { chemical: "1.73e3", electrical: "-9.65e2", total: "7.64e2" },
      choices: {},
    },
    {
      number: 19,
      numeric: { diffusion_step: "2.50", combined_step: "2.00" },
      choices: {},
    },
    {
      number: 20,
      numeric: { ratio: "2.00", alpha: "2.00", beta: "4.00" },
      choices: {},
    },
    {
      number: 21,
      numeric: { cost: "1.78e3", count: "5" },
      choices: { meaning: "2" },
    },
    {
      number: 22,
      numeric: { first: "0.200", second: "0.600", third: "0.200" },
      choices: { fourth: "0" },
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/transport");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/transport/lesson/transport-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 20 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="transport-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(6);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("organic semester foundations and paper assignments deliver and grade exact structural counts", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 17,
      numeric: { neighbor: "2", first_distance: "3", other_distance: "2" },
      choices: {},
    },
    {
      number: 18,
      numeric: { orders: "6", valid: "1" },
      choices: { reason: "2" },
    },
    {
      number: 19,
      numeric: { first: "1.05", other: "0.450", remaining: "0.500" },
      choices: {},
    },
    {
      number: 20,
      numeric: { carbon: "10", hydrogen: "12", centers: "0", dbe: "5" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/organic-chemistry");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/organic-chemistry/lesson/organic-chemistry-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 19 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="organic-chemistry-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(4);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("statics semester foundations and paper assignments deliver compatibility and material-history grading", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: { prop: "3.38e2", fixed_force: "5.62e2", couple: "1.69e2" },
      choices: {},
    },
    {
      number: 17,
      numeric: {
        yield_strain: "2.00e-3",
        plastic_strain: "3.00e-3",
        extension: "6.00e-4",
      },
      choices: {},
    },
    {
      number: 18,
      numeric: { prop: "1.62e2", fixed_force: "4.38e2", couple: "1.65e2" },
      choices: {},
    },
    {
      number: 19,
      numeric: {
        plastic_strain: "4.00e-3",
        extension: "6.00e-4",
        input: "1.20e6",
        recoverable: "2.40e5",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/statics-materials");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/statics-materials/lesson/statics-materials-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 18 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="statics-materials-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(4);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("genetics semester foundations and evidence assignments deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    { number: 19, numeric: { groups: "2" }, choices: { order: "0" } },
    {
      number: 20,
      numeric: {
        dna_fraction: "0.600",
        rna_fraction: "0.429",
        per_copy: "0.500",
      },
      choices: {},
    },
    {
      number: 21,
      numeric: { mean: "0.871", selected: "0.245", next: "0.246" },
      choices: {},
    },
    {
      number: 22,
      numeric: { groups: "3", fraction: "0.0100", map: "1.00" },
      choices: {},
    },
    {
      number: 23,
      numeric: { dna: "0.667", rna: "0.500", per_copy: "0.500" },
      choices: {},
    },
    {
      number: 24,
      numeric: {
        mean: "0.925",
        selected: "0.209",
        next: "0.210",
        aa_f: "0.0812",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/genetics");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/genetics/lesson/genetics-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 22 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="genetics-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
      if (check.number === 23) {
        const href = await page
          .getByRole("link", {
            name: "genome-evidence-counts.csv",
            exact: true,
          })
          .getAttribute("href");
        expect(href).toBe(
          "/api/v1/courses/genetics/resources/assignments/genome-evidence-counts.csv",
        );
        const data = await page.request.get(href!);
        expect(await data.body()).toEqual(
          await readFile(
            new URL(
              "../../content/courses/genetics/assignments/genome-evidence-counts.csv",
              import.meta.url,
            ),
          ),
        );
      }
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(6);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("calculus one semester packets deliver mixed reasoning and integral practice", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: { left: "1.50", right: "4.50", trapezoid: "3.00" },
      choices: {},
    },
    {
      number: 17,
      numeric: { value: "6.00", slope: "1.00" },
      choices: { second: "1" },
    },
    {
      number: 18,
      numeric: { first: "-0.800", second: "-0.336", inverse: "-1.25" },
      choices: {},
    },
    {
      number: 19,
      numeric: { cut: "1.92", volume: "1.20e2", capped: "1.16e2" },
      choices: {},
    },
    {
      number: 20,
      numeric: {
        net: "4.00",
        distance: "8.50",
        final: "11.0",
        minimum: "4.75",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/calculus-1");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/calculus-1/lesson/calculus-1-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number === 16 ? 4 : 3,
      );
      const question = page.locator(
        `[data-question-id="calculus-1-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(5);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("mechanics semester packets deliver constrained and contact motion grading", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: { acceleration: "1.96", tension1: "35.3", tension2: "39.2" },
      choices: {},
    },
    {
      number: 17,
      numeric: { time: "0.510", speed: "2.00", spin: "20.0" },
      choices: {},
    },
    {
      number: 18,
      numeric: {
        collision_speed: "0.200",
        collision_loss: "2.16",
        capture_mass: "4.00",
        capture_speed: "1.50",
        capture_energy: "4.50",
      },
      choices: {},
    },
    {
      number: 19,
      numeric: { acceleration: "3.92", tension1: "27.5", tension2: "35.3" },
      choices: {},
    },
    {
      number: 20,
      numeric: { time: "0.326", speed: "2.00", spin: "16.7", loss: "1.68" },
      choices: {},
    },
    {
      number: 21,
      numeric: { position: "0.100", velocity: "-0.0400", energy: "0.0208" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/physics-mechanics");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/physics-mechanics/lesson/physics-mechanics-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 18 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="physics-mechanics-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
      if (check.number === 21) {
        const href = await page
          .getByRole("link", { name: "oscillator-reference.csv", exact: true })
          .getAttribute("href");
        expect(href).toBe(
          "/api/v1/courses/physics-mechanics/resources/assignments/oscillator-reference.csv",
        );
        const data = await page.request.get(href!);
        expect(await data.body()).toEqual(
          await readFile(
            new URL(
              "../../content/courses/physics-mechanics/assignments/oscillator-reference.csv",
              import.meta.url,
            ),
          ),
        );
      }
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(6);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("linear algebra semester proof packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 15,
      numeric: { l31: "2.00", l32: "1.00", u33: "-1.00", determinant: "1.00" },
      choices: {},
    },
    {
      number: 16,
      numeric: { x1: "2.00", x2: "0.500", norm: "2.06", eigenspace: "1" },
      choices: {},
    },
    {
      number: 17,
      numeric: { rank: "2", nullity: "1", left_nullity: "2" },
      choices: {},
    },
    {
      number: 18,
      numeric: { intercept: "1.17", slope: "0.500", residual: "0.408" },
      choices: {},
    },
    {
      number: 19,
      numeric: { first: "1.80", second: "0.360", radius: "0.600" },
      choices: {},
    },
    {
      number: 20,
      numeric: { first: "1.00", second: "1.00", third: "1.00", norm: "1.73" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/linear-algebra");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/linear-algebra/lesson/linear-algebra-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 17 ? 4 : 3,
      );
      const question = page.locator(
        `[data-question-id="linear-algebra-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(6);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("chemistry two semester evidence packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: { alpha: "0.333", conditional: "1.25e3", complex: "9.00e-4" },
      choices: {},
    },
    {
      number: 17,
      numeric: {
        electrons: "5",
        high_unpaired: "5",
        low_unpaired: "1",
        low_pairs: "2",
      },
      choices: {},
    },
    {
      number: 18,
      numeric: { observed: "2.00e-4", plateau: "4.00e-4", half: "6.00e-4" },
      choices: {},
    },
    {
      number: 19,
      numeric: {
        alpha: "0.800",
        complex: "8.00e-4",
        metal: "4.00e-4",
        ligand: "8.00e-4",
      },
      choices: {},
    },
    {
      number: 20,
      numeric: { rate: "3.00e-4", half: "5.00e-4", plateau: "6.00e-4" },
      choices: {},
    },
    {
      number: 21,
      numeric: {
        splitting: "1.84e2",
        difference: "5.96",
        unpaired: "4",
        moment: "4.90",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/general-chemistry-2");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/general-chemistry-2/lesson/general-chemistry-2-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 19 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="general-chemistry-2-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
      if (check.number === 20) {
        const href = await page
          .getByRole("link", { name: "reference CSV", exact: true })
          .getAttribute("href");
        expect(href).toBe(
          "/api/v1/courses/general-chemistry-2/resources/assignments/ligand-exchange-reference.csv",
        );
        const data = await page.request.get(href!);
        expect(await data.body()).toEqual(
          await readFile(
            new URL(
              "../../content/courses/general-chemistry-2/assignments/ligand-exchange-reference.csv",
              import.meta.url,
            ),
          ),
        );
      }
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(6);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("physiology semester model packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 17,
      numeric: { filtered: "10.0", excreted: "0.0250", fraction: "0.00250" },
      choices: {},
    },
    {
      number: 18,
      numeric: { water: "0.100", signal: "-0.100", initial: "0.100" },
      choices: {},
    },
    {
      number: 19,
      numeric: { content_one: "162", content_two: "90.0", mixed: "138" },
      choices: {},
    },
    {
      number: 20,
      numeric: { tau: "5.00", steady: "-50.0", voltage: "-53.7" },
      choices: {},
    },
    {
      number: 21,
      numeric: {
        mixed: "1.60e2",
        equivalent: "50.0",
        delivery: "6.40e2",
        uptake: "3.20e2",
      },
      choices: {},
    },
    {
      number: 22,
      numeric: {
        filtered: "10.8",
        excreted: "0.0270",
        fraction: "0.00250",
        urine_flow: "1.80",
        urine_na: "15.0",
      },
      choices: {},
    },
    {
      number: 23,
      numeric: {
        water: "0.100",
        signal: "-0.200",
        real: "-0.750",
        imaginary: "0.968",
        initial: "0.150",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/physiology");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/physiology/lesson/physiology-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 20 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="physiology-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("differential equations semester method packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: { factor: "7.39", state: "3.27", derivative: "-0.541" },
      choices: {},
    },
    {
      number: 17,
      numeric: {
        amplitude: "0.900",
        lag: "0.785",
        sine: "0.637",
        cosine: "-0.637",
      },
      choices: {},
    },
    {
      number: 18,
      numeric: { radius: "2.00", period: "3.14", exponent: "-8.00" },
      choices: {},
    },
    {
      number: 19,
      numeric: { factor: "2.72", state: "1.74", particular: "1.00" },
      choices: {},
    },
    {
      number: 20,
      numeric: {
        first_state: "0.125",
        velocity: "0.393",
        second_state: "0.393",
      },
      choices: {},
    },
    {
      number: 21,
      numeric: {
        first: "0.528",
        second: "0.632",
        steady_first: "2.00",
        steady_second: "1.00",
      },
      choices: {},
    },
    {
      number: 22,
      numeric: {
        cycle_radius: "0.500",
        period: "3.14",
        exponent: "-0.500",
        observed_radius: "0.354",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/differential-equations");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/differential-equations/lesson/differential-equations-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 19 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="differential-equations-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("bioreactors semester evidence packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: {
        loss: "0.0700",
        growth: "0.100",
        substrate: "0.100",
        biomass: "1.58",
      },
      choices: {},
    },
    {
      number: 17,
      numeric: { liquid: "0.632", probe: "0.473", curvature: "3.00" },
      choices: {},
    },
    {
      number: 18,
      numeric: { first: "0.800", second: "0.400", mean: "0.600" },
      choices: {},
    },
    {
      number: 19,
      numeric: {
        loss: "0.120",
        growth: "0.150",
        substrate: "0.167",
        biomass: "1.38",
      },
      choices: {},
    },
    {
      number: 20,
      numeric: {
        liquid: "0.632",
        probe: "0.400",
        curvature: "4.50",
        apparent: "0.765",
      },
      choices: {},
    },
    {
      number: 21,
      numeric: { first: "0.880", second: "0.480", mean: "0.613" },
      choices: {},
    },
    {
      number: 22,
      numeric: {
        minus_minus: "12.0",
        plus_minus: "10.0",
        minus_plus: "4.00",
        plus_plus: "14.0",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/bioreactors");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/bioreactors/lesson/bioreactors-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 19 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="bioreactors-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
      if (check.number === 20 || check.number === 22) {
        const resource =
          check.number === 20
            ? {
                name: "analytic probe reference CSV",
                file: "probe-response-reference.csv",
              }
            : {
                name: "synthetic factorial run CSV",
                file: "process-evidence-factorial.csv",
              };
        const href = await page
          .getByRole("link", { name: resource.name, exact: true })
          .getAttribute("href");
        expect(href).toBe(
          `/api/v1/courses/bioreactors/resources/assignments/${resource.file}`,
        );
        const data = await page.request.get(href!);
        expect(await data.body()).toEqual(
          await readFile(
            new URL(
              `../../content/courses/bioreactors/assignments/${resource.file}`,
              import.meta.url,
            ),
          ),
        );
      }
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("electromagnetism semester boundary packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    { number: 17, numeric: { fraction: "0.0625", field: "31.3" }, choices: {} },
    {
      number: 18,
      numeric: { coupling: "0.500", energy: "0.130" },
      choices: {},
    },
    {
      number: 19,
      numeric: { field: "1.88", one_side: "0.00471", total: "0.00942" },
      choices: {},
    },
    {
      number: 20,
      numeric: { field: "20.0", boundary: "8.79", axis: "10.8" },
      choices: {},
    },
    {
      number: 21,
      numeric: {
        energy: "0.180",
        first_voltage: "0.0300",
        second_voltage: "0.210",
        rate: "0.270",
      },
      choices: {},
    },
    {
      number: 22,
      numeric: { field: "5.65", one_side: "0.0424", total: "0.0848" },
      choices: {},
    },
    {
      number: 23,
      numeric: {
        final: "2.00",
        dissipated: "24.0",
        tau: "2.67",
        current: "3.00",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/physics-em");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/physics-em/lesson/physics-em-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 20 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="physics-em-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("calculus two semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    { number: 16, numeric: { length: "2.83", lateral: "53.3" }, choices: {} },
    {
      number: 17,
      numeric: { global: "1.00", restricted: "0.000977", index: "10" },
      choices: {},
    },
    {
      number: 18,
      numeric: { rational: "0.0628", parts: "0.184" },
      choices: { method: "1" },
    },
    {
      number: 19,
      numeric: { lateral: "28.1", volume: "13.6", closed: "59.5" },
      choices: {},
    },
    {
      number: 20,
      numeric: { bound: "0.217", index: "22027" },
      choices: { classification: "2" },
    },
    {
      number: 21,
      numeric: {
        approximation: "0.119792",
        bound: "0.000521",
        error: "0.000460",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/calculus-2");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/calculus-2/lesson/calculus-2-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 18 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="calculus-2-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(6);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("circuits semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    { number: 16, numeric: { diode: "0.535", source: "1.54" }, choices: {} },
    { number: 17, numeric: { current: "1.13", drain: "8.63" }, choices: {} },
    { number: 18, numeric: { loop: "1.00", gain: "1.00e2" }, choices: {} },
    {
      number: 19,
      numeric: { diode: "0.539", source: "2.54", resistance: "26.0" },
      choices: {},
    },
    {
      number: 20,
      numeric: {
        current: "1.00",
        drain: "7.00",
        transconductance: "1.00",
        gain: "-2.00",
      },
      choices: {},
    },
    {
      number: 21,
      numeric: {
        loop: "3.00",
        gain: "30.0",
        pair_real: "-279",
        pair_imaginary: "1.25e3",
      },
      choices: {},
    },
    {
      number: 22,
      numeric: { bandwidth: "62.5", rms: "316", step: "0.594" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/circuits");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/circuits/lesson/circuits-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 19 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="circuits-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("statistics semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 18,
      numeric: { normalization: "1.00", mean_x: "0.667", mean_y: "0.333" },
      choices: {},
    },
    { number: 19, numeric: { rate: "0.125", mean: "8.00" }, choices: {} },
    { number: 20, numeric: { mean: "4.86", variance: "2.29" }, choices: {} },
    {
      number: 21,
      numeric: { intercept: "1.00", slope_x: "2.00", slope_z: "3.00" },
      choices: {},
    },
    {
      number: 22,
      numeric: {
        pairs: "10",
        mean: "0.800",
        variance: "0.360",
        covariance: "-0.0600",
      },
      choices: {},
    },
    {
      number: 23,
      numeric: { coverage: "0.875", miss: "0.125", upper: "0.602" },
      choices: { bootstrap: "1" },
    },
    {
      number: 24,
      numeric: {
        intercept: "3.00",
        slope_x: "4.00",
        slope_z: "-2.00",
        sse: "3.00",
      },
      choices: {},
    },
    {
      number: 25,
      numeric: {
        rate: "0.250",
        mean: "4.00",
        information: "48.0",
        standard_error: "0.144",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/statistics");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/statistics/lesson/statistics-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 22 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="statistics-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(8);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("robotics semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 15,
      numeric: { m11: "2.67", m12: "0.833", m22: "0.333" },
      choices: {},
    },
    { number: 16, numeric: { tangent: "1.00", reaction: "5.00" }, choices: {} },
    { number: 17, numeric: { speed: "0.320", motion: "0.0320" }, choices: {} },
    {
      number: 18,
      numeric: {
        shoulder: "1.63",
        elbow: "0.315",
        kinetic: "0.0509",
        potential: "0.240",
      },
      choices: {},
    },
    {
      number: 19,
      numeric: { tangent: "3.00", reaction: "5.00", effective_mass: "3.00" },
      choices: {},
    },
    {
      number: 20,
      numeric: { speed: "0.550", motion: "0.0275", margin: "0.0125" },
      choices: {},
    },
    {
      number: 21,
      numeric: {
        shoulder_request: "1.60",
        elbow_request: "0.333",
        shoulder_acceleration: "2.38",
        elbow_acceleration: "-2.88",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/robotics");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/robotics/lesson/robotics-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 18 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="robotics-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("cellular biomechanics semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: {
        gamma: "0.0200",
        stress_xx: "0.100",
        stress_yy: "0.120",
        shear: "0.0600",
      },
      choices: {},
    },
    { number: 17, numeric: { radius: "42.4", force: "10.7" }, choices: {} },
    {
      number: 18,
      numeric: { hazard: "0.859", survival: "0.424" },
      choices: {},
    },
    {
      number: 19,
      numeric: {
        stress_xx: "0.0900",
        stress_yy: "-0.0200",
        shear: "0.0400",
        energy: "1.40",
      },
      choices: {},
    },
    { number: 20, numeric: { radius: "25.0", force: "12.6" }, choices: {} },
    { number: 21, numeric: { mode: "5.55", median: "5.31" }, choices: {} },
    {
      number: 22,
      numeric: {
        normal_a: "0.0700",
        normal_b: "0.100",
        shear_a: "0.0600",
        shear_b: "0.0300",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/cellular-biomechanics");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/cellular-biomechanics/lesson/cellular-biomechanics-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 19 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="cellular-biomechanics-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("signals control semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 17,
      numeric: { area: "2.00", transform: "1.27", zero: "3.14" },
      choices: {},
    },
    {
      number: 18,
      numeric: { pole: "6.00", gain: "12.0", zero: "2.67" },
      choices: {},
    },
    {
      number: 19,
      numeric: { controllable: "2", observable: "2", dc: "0.167" },
      choices: {},
    },
    {
      number: 20,
      numeric: { trace: "1.40", determinant: "0.600" },
      choices: {},
    },
    {
      number: 21,
      numeric: {
        input_energy: "2.00",
        magnitude: "1.27",
        output_energy: "2.67",
        transform_real: "-1.62",
      },
      choices: {},
    },
    {
      number: 22,
      numeric: { pole: "8.00", gain: "19.0", zero: "3.42" },
      choices: {},
    },
    {
      number: 23,
      numeric: { k_one: "17.0", k_two: "6.00", reference: "21.0" },
      choices: {},
    },
    {
      number: 24,
      numeric: {
        trace: "1.00",
        determinant: "0.250",
        pole: "0.500",
        sample_two: "0.750",
      },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/signals-control");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/signals-control/lesson/signals-control-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 21 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="signals-control-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(8);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("calculus three semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 15,
      numeric: {
        partial_x: "-0.500",
        partial_y: "-1.00",
        surface_factor: "1.50",
      },
      choices: {},
    },
    { number: 16, numeric: { jacobian: "8.00", radius: "2.00" }, choices: {} },
    {
      number: 17,
      numeric: { y_first: "0.785", x_first: "-0.785" },
      choices: {},
    },
    {
      number: 18,
      numeric: {
        partial_x: "-0.354",
        partial_y: "-0.707",
        new_z: "1.42",
        error: "0.00177",
      },
      choices: {},
    },
    {
      number: 19,
      numeric: {
        area: "4.00",
        total: "6.00",
        average: "1.50",
        jacobian: "2.00",
      },
      choices: {},
    },
    {
      number: 20,
      numeric: { top: "11.5", bottom: "-3.14", net: "8.38", volume: "1.57" },
      choices: {},
    },
    {
      number: 21,
      numeric: { y_first: "0.785", x_first: "-0.785", ratio_three: "0.464" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/calculus-3");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(`/#/course/calculus-3/lesson/calculus-3-${check.number}`);
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 18 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="calculus-3-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(7);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("chemistry one semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 15,
      numeric: { photon: "0.556", ionization: "1.00" },
      choices: {},
    },
    { number: 16, numeric: { plus: "-1.17", minus: "-0.750" }, choices: {} },
    {
      number: 17,
      numeric: { photon: "1.69", ionization: "0.563" },
      choices: {},
    },
    {
      number: 18,
      numeric: { plus: "-2.27", minus: "-1.67", coefficient: "0.674" },
      choices: {},
    },
    {
      number: 19,
      numeric: {
        extent: "0.250",
        molecules: "1.75",
        pressure: "0.875",
        atoms: "2.50",
      },
      choices: {},
    },
    {
      number: 20,
      numeric: { offset: "0.0200", x: "0.200", y: "0.300", total: "0.500" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/general-chemistry-1");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/general-chemistry-1/lesson/general-chemistry-1-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 17 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="general-chemistry-1-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(6);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("biomaterials semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 16,
      numeric: { one: "0.400", two: "0.600", ceiling: "0.800" },
      choices: {},
    },
    {
      number: 17,
      numeric: { attachment: "0.600", fold: "2.00", net_rate: "0.347" },
      choices: {},
    },
    {
      number: 18,
      numeric: { graft: "0.675", cosine: "0.175", angle: "79.9" },
      choices: {},
    },
    {
      number: 19,
      numeric: {
        attachment: "0.500",
        net_rate: "0.231",
        signal_fold: "3.00",
        alpha_ratio: "1.50",
      },
      choices: {},
    },
    {
      number: 20,
      numeric: {
        stiffness: "0.0625",
        permeability: "6.75",
        upper_porosity: "0.800",
      },
      choices: { decision: "1" },
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/biomaterials");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/biomaterials/lesson/biomaterials-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 18 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="biomaterials-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(5);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("geroscience semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    {
      number: 18,
      numeric: { mean: "5.20", minimum: "3.20", divisions: "4" },
      choices: {},
    },
    {
      number: 19,
      numeric: { mean: "4.60", minimum: "3.10", without: "5", with: "10" },
      choices: {},
    },
    {
      number: 20,
      numeric: {
        a_difference: "0.400",
        b_difference: "0.100",
        contrast: "0.300",
      },
      choices: {},
    },
    {
      number: 21,
      numeric: { fraction: "0.520", cells: "520", naive: "0.600" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/geroscience");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/geroscience/lesson/geroscience-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number === 18 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="geroscience-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(4);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

test("biochemistry semester reasoning packets deliver and grade", async ({
  page,
}) => {
  const checks: {
    number: number;
    numeric: Record<string, string>;
    choices: Record<string, string>;
  }[] = [
    { number: 28, numeric: { initial: "3.00", doubled: "3.27" }, choices: {} },
    {
      number: 29,
      numeric: { atp: "40", equivalents: "80", bonds: "39" },
      choices: {},
    },
    { number: 30, numeric: { co2: "3", atp: "9", nadph: "6" }, choices: {} },
    {
      number: 31,
      numeric: { ion: "-2.77", cycle: "-1.39", stall: "256", pump: "3" },
      choices: {},
    },
    {
      number: 32,
      numeric: { output: "1.33", co2: "4.00", atp_left: "8.00" },
      choices: {},
    },
  ];
  await page.goto("/#/account");
  await page
    .getByRole("button", { name: "Start guest session", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Guest session", exact: true }),
  ).toBeVisible();
  try {
    await page.goto("/#/course/biochemistry");
    await page
      .getByRole("button", { name: "Enroll in partial course", exact: true })
      .click();
    await expect(page.getByText("Enrolled", { exact: true })).toBeVisible();
    for (const check of checks) {
      await page.goto(
        `/#/course/biochemistry/lesson/biochemistry-${check.number}`,
      );
      await expect(page.locator(".lesson-reader")).toBeVisible();
      await expect(page.locator("[data-question-id]")).toHaveCount(
        check.number < 31 ? 4 : 2,
      );
      const question = page.locator(
        `[data-question-id="biochemistry-${check.number}:depth-1"]`,
      );
      for (const [field, value] of Object.entries(check.numeric))
        await question.locator(`input[name="${field}"]`).fill(value);
      for (const [field, value] of Object.entries(check.choices))
        await question.locator(`select[name="${field}"]`).selectOption(value);
      await question
        .getByRole("button", { name: "Submit practice response" })
        .click();
      const points =
        Object.keys(check.numeric).length + Object.keys(check.choices).length;
      await expect(
        question.getByRole("region", { name: "Submission feedback" }),
      ).toContainText(`${points} / ${points} practice points`);
      expect(
        (
          await new AxeBuilder({ page })
            .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
            .analyze()
        ).violations,
      ).toEqual([]);
    }
    const exported = await (
      await page.request.get("/api/v1/learner/export")
    ).json();
    expect(exported.attempts).toHaveLength(5);
    expect(exported.graded_submissions).toEqual([]);
  } finally {
    const status = await page.evaluate(async () => {
      const session = await (await fetch("/api/v1/auth/session")).json();
      if (!session.user) return null;
      return (
        await fetch("/api/v1/learner", {
          method: "DELETE",
          headers: { "X-CSRF-Token": session.csrf_token },
        })
      ).status;
    });
    if (status !== null) expect(status).toBe(204);
  }
});

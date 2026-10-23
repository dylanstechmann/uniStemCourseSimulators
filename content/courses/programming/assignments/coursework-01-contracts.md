# Assignment 1: a validated observation table

**Open, ungraded implementation practice.** This original assignment was developed with substantial AI assistance. Run your own code locally; the app checks selected arithmetic and interpretation fields but does not run or grade your implementation. Proposed placement: week 4. Time is not measured. Save your source, tests and report locally; a lesson note can hold your own progress observations.

## The input and the question

The [observation table](semester-observations.csv) contains eight synthetic rows. Each row names a record, specimen, technical-repeat number, observed length and unit. The scientific question is the mean specimen length among specimens with valid observations, with each specimen receiving equal weight. Technical repeats describe one specimen rather than new independently sampled specimens. The identifiers carry no real personal information.

Accept only finite, strictly positive lengths in `um` or `mm`. Convert accepted lengths to millimeters using 1000 um = 1 mm. Record identifiers must be nonempty. For this assignment only, repeated rows with the same identifier and identical fields use an explicit first-occurrence policy: retain the first valid occurrence and log each later identical occurrence as a duplicate. If an identifier reappears with conflicting fields, reject all occurrences of that identifier and report a conflict. Do not silently average conflicting records.

These are declared teaching contracts. They are not universal rules for experimental data. A negative value might be meaningful for another quantity, and a missing observation requires a reasoned policy. Here its contract is deliberately simple so validation outcomes can be checked independently.

## Part A: parse without losing evidence

Write a parser that separates text ingestion from scientific validation. Keep an immutable representation of each original row and its row number. Return accepted normalized records plus a rejection/duplicate ledger identifying the original row, reason and original fields. A nonnumeric value and an unsupported unit should produce different reasons. `NaN` can parse as a floating-point value but still fails the finite-value contract.

Make validation a pure function where practical: the same input records and policy produce the same output without changing a global list or generator. Avoid printing an error and returning zero for an invalid length. Zero would look like a valid numerical observation downstream and bias the result. Decide and document whether a row with several defects receives one primary reason or all applicable reasons.

## Part B: aggregate at the stated unit of analysis

For each specimen with accepted observations, compute its mean normalized length. Then average those specimen means with equal specimen weights. Report the number of accepted records, rejected/duplicate rows and represented specimens separately. A specimen without valid observations contributes to the missingness ledger, not an invented zero.

Explain why pooling every technical reading can change the estimand when repeat counts differ. Demonstrate it on a separate tiny example: specimen A has readings 1 and 3, specimen B has one reading 10. The equally weighted specimen mean is (2+10)/2=6; the pooled reading mean is 14/3. Neither arithmetic operation is inherently impossible, but they answer different questions. The declared target here is the first.

## Part C: tests that can falsify the implementation

Create a known-answer test for a clean one-specimen table with mixed supported units. Add tests for a zero length, infinity, an unknown unit, an empty identifier, an identical duplicate and a conflicting duplicate. Test that permuting clean input rows does not change normalized specimen means. For duplicate conflicts, permuting rows should not change which identifier is excluded under the all-conflicting-occurrences policy.

Verify that your program does not mutate the input records. Use both an empty input and an all-invalid input to decide a clear return/failure contract for an undefined overall mean. A test that compares the program to the same function called twice establishes determinism only; it cannot independently establish correctness.

## Part D: an auditable report

Show the original-to-normalized unit map, acceptance ledger, specimen summary table and final estimand with millimeter units. List the rules that were applied before looking at the resulting mean. Record the input file hash, program version and software version. Distinguish decisions authored by you from suggestions or calculations provided by tools, including AI assistance.

Draw a plot of the valid specimen means, label its units and identify the specimen as the plotted unit. Give a text description of the same findings. Do not display technical repeats as independent specimens merely to make the figure appear better sampled. Missing specimens and rejected observations should remain visible in the report rather than disappearing from its denominator description.

## Self-review after attempting the assignment

The first four rows are valid; their lengths become 0.100, 0.120, 0.200 and 0.220 mm. The later identical `r4` occurrence is logged as a duplicate. The `NaN`, negative and unsupported-unit rows fail their respective contracts. Thus four observations remain, with four excluded rows under this dataset's policy. S1 has mean 0.110 mm and S2 0.210 mm; their equally weighted mean is 0.160 mm. Only two specimens contribute to that mean.

These reference values do not certify the implementation. Your tests must also handle the conflicting-ID case, which this small file does not contain. A correct mean can occur accidentally when several errors cancel. Inspect the ledger and independent tests as well as the final number.

## Scope and provenance

This packet integrates the existing parsing, contracts, units, testing and cost lessons. Its records and tasks are original CC BY 4.0 material. [MIT OCW 2.086 Fall 2014 syllabus](https://ocw.mit.edu/courses/2-086-numerical-computation-for-mechanical-engineers-fall-2014/pages/syllabus/) is a link-only comparator for implementation-based numerical coursework; no assignment or code was imported. Scientific review, code review and measured workload remain open.

# Laboratory Measurement scope crosswalk

This crosswalk compares the local package, version 0.1.0, with MIT OpenCourseWare 5.310 Laboratory Chemistry, Fall 2019 ([syllabus](https://ocw.mit.edu/courses/5-310-laboratory-chemistry-fall-2019/pages/syllabus/), [calendar](https://ocw.mit.edu/courses/5-310-laboratory-chemistry-fall-2019/pages/calendar/)). It was compiled with AI assistance on 2026-10-30 from the syllabus's course description and the calendar's lecture and experiment titles. It is an agent-run comparison, not a review by the owner or by a laboratory instructor. Topic alignment establishes no equivalence, credit or endorsement.

5.310 is a full-semester laboratory course built around five experiments (ferrocene, the Ellen Swallow Richards lab, essential oils, esterification and catalase) with lectures on the chemistry and instruments behind them. This package is a six-week foundation module on measurement, so most of 5.310's instrumental and synthetic scope is deliberately outside it. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **shallow** means part of it is taught; **absent** means no local instruction; **local extension** means 5.310's published titles and description do not name the topic.

| Topic | MIT 5.310 Fall 2019 | Local lessons | Status |
| --- | --- | --- | --- |
| Laboratory safety | Week 1 mandatory safety lecture | — | Absent here by design: biosafety is layer 1 of the track; the cabinet simulation exists on the bench page |
| Measurement of pH | Named in the course description | [5](modules/05-ph-measurement-and-buffer-preparation.md) | Covered: calibration, slope acceptance, mV-to-pH conversion, buffer planning and temperature |
| Visible–ultraviolet spectrophotometry | Named in the course description | [6](modules/06-spectrophotometry-and-standard-curves.md) | Covered for absorbance, Beer–Lambert, blanks and standard curves; instrument optics are not taught |
| Error analysis and data analysis | L4, "What's Significant in Laboratory Measurement? Error Analysis"; description names data analysis | [2](modules/02-dilutions-and-dilution-series.md), [3](modules/03-measuring-volume-and-checking-pipettes.md), [4](modules/04-balances-and-weighing.md), [6](modules/06-spectrophotometry-and-standard-curves.md) | Shallow: systematic and random error, propagation along a series, minimum weight and residuals; formal uncertainty budgets are not taught |
| Preparation of chemical materials | Named in the course description | [1](modules/01-concentration-and-solution-preparation.md) | Covered for solutions; synthesis and purification are absent |
| Lab notebooks and reports | L3, "Writing Up the Lab Report"; notebooks referenced in the syllabus | — | Absent: record-keeping appears only as advice inside lessons |
| Kinetics | Named in the description; catalase experiment | — | Absent |
| Gas and liquid chromatography, IR, NMR, mass spectrometry, polarimetry, X-ray diffraction | Named in the description; lectures L13–L15 | — | Absent by design |
| Organic synthesis | Ferrocene, essential oils and esterification experiments | — | Absent by design |
| Volumetric glassware and micropipettes | Not named in the published titles or description | [3](modules/03-measuring-volume-and-checking-pipettes.md) | Local extension, with the gravimetric pipette simulation |
| Balances and weighing | Not named | [4](modules/04-balances-and-weighing.md) | Local extension |
| Dilution series and plate counts | Not named | [2](modules/02-dilutions-and-dilution-series.md) | Local extension, with the BAM plate-count simulation |
| Graded laboratory reports, quizzes and oral reports | Five reports, quizzes and an oral report | Open practice only | Absent by design: all practice is formative |

## Remaining gaps

- Laboratory notebooks, data integrity and report writing.
- Titration and volumetric analysis; kinetics measurements.
- A formal treatment of measurement uncertainty (uncertainty budgets, coverage factors beyond the minimum-weight example).
- Review by a qualified laboratory instructor, measured workload and any graded assessment.

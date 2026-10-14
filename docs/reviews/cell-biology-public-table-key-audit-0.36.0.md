# Cell Biology public table-key source audit (0.36.0)

**Date:** 2026-10-10  
**Scope:** all public question-bank `file_upload` items whose validator checks contain numeric `count` or `mean` calculations.  
**Review status:** author-side regression only. This verifies consistency between public answer specifications and the referenced synthetic source data; it is not independent scientific, assessment, or accessibility review.

The regression test reads each source CSV, selects rows by the declared condition and timepoint, verifies distinct replicate IDs, recomputes means and counts, compares source values with the calculation arrays stored in the question, and checks each result against its declared tolerance. The image-quantification item derives each batch percentage from positive and viable nuclei. The enzyme-rate homework filters to 40 μM substrate, and the lineage lab filters to day 8. The first summary exercise supplies replicate values in its prompt rather than a separate CSV.

| Public practice item | Source values | Checked cells |
| --- | --- | ---: |
| `cell-biology-4:csv-summary-table` | Replicate values printed in the question prompt | 4 |
| `cell-biology-11:image-quantification-summary` | `content/courses/cell-biology/labs/image-counts.csv` | 4 |
| `cell-biology-hw1:sorting-summary` | `content/courses/cell-biology/assignments/homework-01-m6p-sorting.csv` | 9 |
| `cell-biology-lab2:summary-table` | `content/courses/cell-biology/labs/signaling-timecourse.csv` | 24 |
| `cell-biology-hw2:rate-summary` | `content/courses/cell-biology/assignments/homework-02-inhibition-rates.csv` | 6 |
| `cell-biology-hw3:lesion-summary` | `content/courses/cell-biology/assignments/homework-03-lesion-removal.csv` | 9 |
| `cell-biology-hw4:chip-reporter-summary` | `content/courses/cell-biology/assignments/homework-04-chip-reporter.csv` | 10 |
| `cell-biology-hw5:layer-summary` | `content/courses/cell-biology/assignments/homework-05-rna-protein.csv` | 10 |
| `cell-biology-hw6:clone-summary` | `content/courses/cell-biology/assignments/homework-06-isogenic-clones.csv` | 6 |
| `cell-biology-hw7:coverslip-summary` | `content/courses/cell-biology/assignments/homework-07-matrix-spreading.csv` | 12 |
| `cell-biology-hw8:state-summary` | `content/courses/cell-biology/assignments/homework-08-cell-state.csv` | 12 |
| `cell-biology-lab3:summary-table` | `content/courses/cell-biology/labs/lineage-timecourse.csv` | 8 |
| **Total** | **12 public practice items** | **114** |

All 114 cells match the source replicate values and recomputed results within their authored tolerances. The regression is [tests/content/test_cell_biology_public_table_keys.py](../../tests/content/test_cell_biology_public_table_keys.py). It does not cover the inactive candidate CSVs, test whether the synthetic designs support their proposed scientific claims, or establish a learner workload. Qualified external review remains open.

# MIL-005 Lecture 595 Distributions and Significance

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-007 Go | pending |

---

## Purpose

Decide whether lecture 595 ("Visualising Distributions and Testing for Statistical Significance") is implemented, tested and documented.

## Deliverable

Code for superimposed histograms, a Kernel Density Estimate (KDE) plot, the SciPy t-test with p-value, the NumPy `where` step, plus tests, the notebook section, a lecture screenshot in README and wiki, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Tests assert the means and the p-value result the lecture states | Pass | Mismatch |
| 2 | Histograms before and after are superimposed with a KDE and a legend | Pass | Missing |
| 3 | Screenshot of lecture 595 is in README and wiki | Present | Missing |
| 4 | Wiki page exists in en, da and ms | Present | Missing |
| 5 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The before and after split |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2, 3, 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-18 — within the one-week personal schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement superimposed histograms | Draw the before and after distributions in one chart with matching bins and a legend. | No | |
| 2 | Implement the KDE plot | Show the Kernel Density Estimate of both periods and explain what it estimates. | No | |
| 3 | Implement the significance test | Use SciPy to run the t-test and return the p-value; interpret it as the lecture does. | No | |
| 4 | Use NumPy where for conditional values | Apply `np.where` to process elements by a condition, as in the lecture. | No | |
| 5 | Write tests for lecture 595 | Pytest tests for the histogram data, the KDE call and the p-value. | No | |
| 6 | Add notebook section and Doxygen comments | Mirror the steps in the notebook and comment the functions for Doxygen. | No | |
| 7 | Capture lecture 595 screenshot and update README | Screenshot from the user's Chrome session, saved under docs, shown in the README. | No | |
| 8 | Write lecture 595 wiki page in en, da and ms | Explain what was gained: distributions, KDE and statistical significance with p-values. | No | |

---

[BC-001]: ../business-case.md

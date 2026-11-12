# MIL-004 Lecture 594 Handwashing Effect

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-006 Go | pending |

---

## Purpose

Decide whether lecture 594 ("The Effect of Handwashing") is implemented, tested and documented.

## Deliverable

Code that computes the monthly death rate, marks the date handwashing became mandatory, splits the data before and after, draws the time series with the highlighted periods and a legend, plus tests, the notebook section, a lecture screenshot in README and wiki, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Tests assert the average monthly death rate before and after handwashing as the lecture states | Pass | Mismatch |
| 2 | The chart highlights the handwashing period and has a configured legend | Pass | Missing |
| 3 | Screenshot of lecture 594 is in README and wiki | Present | Missing |
| 4 | Wiki page exists in en, da and ms | Present | Missing |
| 5 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Monthly data and chart helpers |

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

2026-11-17 — within the one-week personal schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Compute the monthly death rate | Add the proportion of deaths per month to the monthly data as the lecture shows. | No | |
| 2 | Split data before and after handwashing | Use the handwashing start date constant to split the data and compute the averages of each period. | No | |
| 3 | Draw the highlighted time series | Plot the rate over time, highlight the handwashing period and configure the legend, as in lecture 594. | No | |
| 4 | Write tests for lecture 594 | Pytest tests for the rate, the split, the averages and the chart structure. | No | |
| 5 | Add notebook section and Doxygen comments | Mirror the steps in the notebook and comment the functions for Doxygen. | No | |
| 6 | Capture lecture 594 screenshot and update README | Screenshot from the user's Chrome session, saved under docs, shown in the README. | No | |
| 7 | Write lecture 594 wiki page in en, da and ms | Explain what was gained: derived columns, splitting on a date and highlighting a period in a time series. | No | |

---

[BC-001]: ../business-case.md

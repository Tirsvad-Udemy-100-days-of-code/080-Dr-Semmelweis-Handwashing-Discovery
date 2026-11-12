# MIL-003 Lecture 593 Clinic Split

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-005 Go | pending |

---

## Purpose

Decide whether lecture 593 ("Analysing the Yearly Data Split By Clinic") is implemented, tested and documented.

## Deliverable

Code for the clinic split: births and deaths per clinic over the years, the clinic comparison chart, the per-clinic death percentage, tests asserting the lecture figures, the notebook section, a lecture screenshot in README and wiki, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Tests assert the per-clinic figures the lecture states | Pass | Mismatch |
| 2 | Clinic 1 and clinic 2 are shown in one chart with a legend | Pass | Missing |
| 3 | Screenshot of lecture 593 is in README and wiki | Present | Missing |
| 4 | Wiki page exists in en, da and ms | Present | Missing |
| 5 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Loaders and chart helpers |

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

2026-11-16 — within the one-week personal schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the yearly clinic split | Functions that select and aggregate yearly births and deaths per clinic, following the lecture 593 challenges and its solutions. | No | |
| 2 | Implement the clinic comparison charts | Charts that compare clinic 1 and clinic 2 with colours and a legend, as in the lecture. | No | |
| 3 | Implement per-clinic death percentage | Compute the share of deaths per clinic and show why clinic 1 was more dangerous. | No | |
| 4 | Write tests for lecture 593 | Pytest tests for the split, the percentages and the chart structure. | No | |
| 5 | Add notebook section and Doxygen comments | Mirror the steps in the notebook and comment the functions for Doxygen. | No | |
| 6 | Capture lecture 593 screenshot and update README | Screenshot from the user's Chrome session, saved under docs, shown in the README. | No | |
| 7 | Write lecture 593 wiki page in en, da and ms | Explain what was gained: splitting data by group and comparing the groups visually. | No | |

---

[BC-001]: ../business-case.md

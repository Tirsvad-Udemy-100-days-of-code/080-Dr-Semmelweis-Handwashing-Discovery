# MIL-002 Lecture 592 Data Exploration

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-004 Go | [ec941c9] |

---

## Purpose

Decide whether lecture 592 ("Preliminary Data Exploration and Visualising Births & Deaths at Vienna Hospital") is implemented, tested and documented.

## Deliverable

Code for challenges 1 to 3 (shape, columns, NaN and duplicates, monthly averages, the 7.08 % death share, the twin-axis births and deaths chart), tests asserting the lecture figures, the notebook section, a lecture screenshot in README and wiki, and the wiki page in en, da and ms.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Tests assert about 267 births and 22.47 deaths per month and 7.08 % deaths | Pass | Mismatch |
| 2 | Chart function returns a Matplotlib figure with twin axes, skyblue and crimson lines, dashed deaths line | Pass | Any missing |
| 3 | Screenshot of lecture 592 is in README and wiki | Present | Missing |
| 4 | Wiki page exists in en, da and ms | Present | Missing |
| 5 | opengrep clean and pytest green | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Skeleton, data and tooling |

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

2026-11-15 — within the one-week personal schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Load yearly and monthly data | Provide loader functions that read the two CSV files into pandas DataFrames with the date column parsed, using names from `constants.py`. | No | |
| 2 | Implement challenge 1 exploration helpers | Functions for shape, column names, years covered, NaN and duplicate checks and monthly averages (about 267 births, 22.47 deaths). | No | |
| 3 | Implement challenge 2 death percentage | Function returning the share of women who died in the 1840s (about 7.08 %). | No | |
| 4 | Implement challenge 3 births and deaths chart | Twin y-axes chart with year and month locators, grid, skyblue and crimson lines, dashed deaths line and widths 3 and 2. | No | |
| 5 | Write tests for lecture 592 | Pytest tests for the loaders, the figures and the chart structure using the Agg backend. | No | |
| 6 | Add notebook section and Doxygen comments | Mirror the steps in the Jupyter notebook and comment every function for Doxygen. | No | |
| 7 | Capture lecture 592 screenshot and update README | Screenshot taken in the user's Chrome session, saved under docs, shown in the README. | No | |
| 8 | Write lecture 592 wiki page in en, da and ms | Explain what was gained: loading data, checking quality, the dangerous 1840s numbers and twin axes. | No | |

---

[BC-001]: ../business-case.md
[ec941c9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/commit/ec941c902d71a90670b723ceb117c73121ec236c

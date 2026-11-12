# MIL-006 Lecture 596 Summary and Release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-008 Go | pending |

---

## Purpose

Decide whether lecture 596 ("Learning Points & Summary") is documented and the project as a whole is complete and publishable.

## Deliverable

The summary wiki page and README section for lecture 596 with screenshot, an end-to-end check of all wiki pages in en, da and ms, a final run of tests and opengrep, and the project status review against the Business Case success criteria.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every success criterion of BC-001 is met | All met | Any open |
| 2 | Wiki has the same page set in en, da and ms and a correct sidebar | Pass | Mismatch |
| 3 | Each of the six lecture steps has a screenshot in README and wiki | 6 of 6 | Fewer |
| 4 | A clean-clone run of both Getting Started guides works | Pass | Fail |
| 5 | pytest green and opengrep clean | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | All lecture steps implemented |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4, 5, 6 and all success criteria | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-19 — within the one-week personal schedule.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture lecture 596 screenshot and update README | Screenshot from the user's Chrome session, saved under docs, shown in the README. | No | |
| 2 | Write lecture 596 summary wiki page in en, da and ms | List the learning points of Day 80: data arguments, histograms and KDE, p-values, highlighting time series, legends and NumPy where. | No | |
| 3 | Check wiki completeness and sidebar in three languages | Same page set in en, da and ms, language lines, sidebar with the Languages section as the wiki process requires. | No | |
| 4 | Verify both Getting Started guides from a clean clone | Follow the Linux and Windows guides in fresh environments (Docker for Linux, Windows Sandbox if needed) and fix gaps. | No | |
| 5 | Review the project against the success criteria | Walk through the Business Case success criteria and record the result. | No | |

---

[BC-001]: ../business-case.md

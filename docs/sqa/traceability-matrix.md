# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [ec941c9] |

---

## Purpose

Tracks backward and forward links between artifact instances so that traceability from objective to gateway to review is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | RC-001 |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | RC-002 |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-006] | - (no checklist; accepted by S01) |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | MIL-002 | RC-003 |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | MIL-003 | RC-004 |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | MIL-004 | RC-005 |
| [MIL-004] | MIL | en | it | [BC-001], [MIL-003] | MIL-005 | RC-006 |
| [MIL-005] | MIL | en | it | [BC-001], [MIL-004] | MIL-006 | RC-007 |
| [MIL-006] | MIL | en | it | [BC-001], [MIL-005] | - | RC-008 |
| [ADR-0001] | ADR | - | - | [BC-001], [PP-001] | - | RC-009 |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | none (no views; see ADR-0001) | [ADR-0001] | pytest tests, MIL-002 to MIL-005 | Covered by tests |
| CN-002 | none | [ADR-0001] | pull request per milestone | Covered |
| CN-003 | none | [ADR-0001] | Getting Started guides, MIL-001 and MIL-006 | Covered |
| CN-004 | none | [ADR-0001] | tests call the assignment's function names | Covered |
| CN-005 | none | [ADR-0001] | repository description, topics, README, MIL-001 | Covered |
| CN-006 | none | [ADR-0001] | pyproject review, MIL-001 | Covered |
| CN-007 | none | [ADR-0001] | screenshots and wiki, MIL-002 to MIL-006 | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |

## Coverage Notes

- There are no use cases, user stories, domain model or design artifacts (ADR-0001), and no Architecture Description or Test Plan; concerns are answered by code, tests and documentation.
- `-` in Upstream means foundational; `-` in Downstream means nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-lecture-592-data-exploration.md
[MIL-003]: ../milestones/mil-003-lecture-593-clinic-split.md
[MIL-004]: ../milestones/mil-004-lecture-594-handwashing-effect.md
[MIL-005]: ../milestones/mil-005-lecture-595-distributions-significance.md
[MIL-006]: ../milestones/mil-006-lecture-596-summary-release.md
[ADR-0001]: ../adr/adr-0001-skip-use-case-artifacts.md
[ec941c9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/commit/ec941c902d71a90670b723ceb117c73121ec236c

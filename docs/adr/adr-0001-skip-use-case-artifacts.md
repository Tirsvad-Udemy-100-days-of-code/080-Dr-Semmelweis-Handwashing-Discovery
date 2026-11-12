# Skip use cases, user stories and presentation pattern

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-009 Go | [ec941c9] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The journey of the `create-project` skill offers candidate user stories, use cases, a use case diagram and design artifacts (step 4a and step 6) before code. This project is a set of pure analysis functions that load two data tables, compute figures and draw charts. It has one actor (S01 running the code, with S02 and S03 only reading), no user interface, no API and no persisted data of its own. Options considered: (a) write the full set of use case artifacts; (b) skip them for a project with a single, obvious goal and describe the tasks as plain technical tasks; the journey allows skipping step 4a with a reason for such a project.

## Decision

The project skips user stories, the use case diagram, use cases and the design artifacts, and records every task as a plain task. There is no presentation layer, so no model-view-viewmodel (MVVM) or model-view-controller (MVC) pattern is chosen.

## Consequences

**Positive:**

- No documents that restate what the lecture steps already say.
- Time goes to code, tests, screenshots and the wiki that S02 and S03 read.

**Negative:**

- No use case to trace a task to; traceability runs from the task to the Business Case objective through its milestone.
- If a user interface is added later, this decision must be revisited and a presentation pattern chosen.

## Affected Artifacts

- [BC-001] — objectives are traced from milestones instead of from use cases.
- [PP-001] — the Stories column of the Gateway Schedule is `none`.

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[ec941c9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/commit/ec941c902d71a90670b723ceb117c73121ec236c

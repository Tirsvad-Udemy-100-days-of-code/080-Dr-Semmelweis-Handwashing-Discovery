# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-002 Go | [ec941c9] |

---

## Purpose

This analysis names the people affected by the Day 80 project, how much power and interest each has, and what each needs from the repository. It uses the power/interest grid and maps each concern to a FURPS+ attribute (Functionality, Usability, Reliability, Performance, Supportability, plus further constraints).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad (personal) | HIGH | HIGH | Manage Closely | A correct, well documented solution that shows what was learned |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository visitors looking for ideas | GitHub community | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies beyond the analysis |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact.
- **Keep Informed (S02, S03):** they cannot change the project but they judge its usefulness; they are informed through the README and the wiki.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture figure is reproduced and proven by a test | Functionality |
| CN-002 | S01 | Work is traceable through plan, branch and pull request | Supportability |
| CN-003 | S02 | The code runs from a clean clone on Windows and Linux with documented commands | Usability |
| CN-004 | S02 | Function names match the assignment so solutions are comparable | Functionality |
| CN-005 | S03 | Description, topics and README explain the repository at a glance | Usability |
| CN-006 | S03 | No runtime dependencies beyond the analysis libraries | Supportability |
| CN-007 | S02 | Each lecture step has a screenshot and a wiki explanation in en, da and ms | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| COM-001 | Pull request on the git host | Once per milestone | Reviewed change with closing issues | Every milestone |
| COM-002 | README and wiki | Once per lecture step | Screenshot and explanation | MIL-002 to MIL-006 |
| COM-003 | Repository description and topics | Once | Discoverability for S03 | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants the course libraries for plotting; S03 wants no runtime dependencies | S01, S03 | Only the analysis libraries are runtime dependencies; tooling is a dev extra |
| Three wiki languages cost time; S02 reads in one language | S01, S02 | English is authoritative; translations follow page by page |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1, 2 and 6 |
| S02 | CN-003, CN-004, CN-007 | [BC-001] objectives 3, 4 and 5 |
| S03 | CN-005, CN-006 | [BC-001] objectives 5 and 6 |

## Sign-Off

Pending review by S01 (in autonomous mode the AI acts as stand-in and records it in the `RC-*`).

---

[BC-001]: ./business-case.md
[ec941c9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/commit/ec941c902d71a90670b723ceb117c73121ec236c

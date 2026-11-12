# MIL-001 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-003 Go | [ec941c9] |

---

## Purpose

Decide whether the project skeleton, tooling, data and documentation base are good enough to build the lecture steps on (lecture 591, "Day 80 Goals").

## Deliverable

A repository with `pyproject.toml`, Python `.gitignore`, `src/` and `tests/` skeleton with `constants.py`, the lecture data and notebook, a `Doxyfile`, a README from the framework template, a Getting Started wiki page (Linux and Windows) in en, da and ms, repository description and topics on the host, and a first screenshot for lecture 591.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m venv .venv`, `pip install -e ".[dev]"` and `pytest` work from a clean clone | Pass | Any step fails |
| 2 | `pyproject.toml` requires Python 3.13 or newer; runtime dependencies are only pandas, NumPy, Matplotlib, SciPy | Pass | Other runtime dependency |
| 3 | Both comma-separated values (CSV) files and the notebook are in the repository | Present | Missing |
| 4 | The repository on the host has a description and at least five topics | Set | Missing |
| 5 | Getting Started exists in en, da and ms with Linux and Windows sections | Present | Page or section missing |
| 6 | opengrep run shows no unaddressed finding | 0 open | Open finding |
| 7 | README follows the framework template and `check-readme.sh` passes | Pass | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001, SA-001, PP-001 accepted | Baseline of the plan-first gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3, 4, 5 and 6 | [BC-001] |
| Success criteria 4, 6, 7, 8 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-14 — within the one-week personal schedule of the Project Plan; the Business Case sets no hard deadline.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Record architecture decision record (ADR) for skipped use-case artifacts | The project is a set of pure analysis functions with one actor, so use cases, user stories and a presentation pattern add nothing. Record the skip in an architecture decision record (ADR) as the create-project skill requires. | No | |
| 2 | Set repository description and topics | Use the Gitea API with the repository token read from `.env` (never stored, imported or tested by the project) to set a one-line description and topics such as python, pandas, matplotlib, scipy, jupyter, data-analysis, udemy, 100-days-of-code. Serves S03. | No | |
| 3 | Add pyproject.toml | Configure Python 3.13 or newer, runtime dependencies pandas, numpy, matplotlib and scipy only, a `dev` extra with pytest and jupyter, pytest settings and the src layout. | No | |
| 4 | Add Python .gitignore | Standard Python ignores plus `.venv/`, `.env`, notebook checkpoints and Doxygen output. | No | |
| 5 | Create src and tests skeleton with constants.py | Create the package under `src/`, an empty `tests/` with conftest using the Agg backend, and `constants.py` holding file names, column names and figures used by the lectures. | No | |
| 6 | Download lecture resources and add data and notebook | Download the zip linked in lecture 591 through the user's Chrome session, put the two CSV files in a data folder and the notebook in a notebooks folder. | No | |
| 7 | Add Doxyfile | Add a Doxyfile configured for the Python sources so the Doxygen comments render. | No | |
| 8 | Write README from the framework template | Use `framework/templates/README-template.md`, include run and test instructions, the venv steps and the lecture 591 screenshot. | No | |
| 9 | Document the local venv and pip upgrade | Describe creating and using `.venv` and `python -m pip install --upgrade pip` in README and wiki. | No | |
| 10 | Write the Getting Started wiki in en, da and ms | Model it on the Getting Started page of project 074 with separate Linux and Windows guides, plus Home and sidebar, and the lecture 591 step with screenshot and what was gained. | No | |
| 11 | Add opengrep local check | Document and run opengrep from `~/.opengrep/cli/latest/opengrep.exe` before every push and fix the findings. | No | |

---

[BC-001]: ../business-case.md
[ec941c9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/commit/ec941c902d71a90670b723ceb117c73121ec236c

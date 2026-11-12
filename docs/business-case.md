# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, accepted after RC-001 Go | pending |

---

## Executive Summary

Day 80 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" asks the participant to play Dr Ignaz Semmelweis and use pandas, Matplotlib and SciPy to show with data that handwashing cut maternal deaths at the Vienna General Hospital. This project turns the six lecture steps of Day 80 (lectures 591 to 596) into a documented, tested and runnable Python 3.13+ repository, with a Jupyter notebook, a `src/` package, pytest tests, and a wiki in English, Danish and Bahasa Malaysia. The result is a portfolio piece that fellow course participants and GitHub visitors can read, run and compare against their own solution.

## Methodological and Standards Foundation

The work follows the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/` (Business Case, Stakeholder Analysis, Project Plan, milestones, then code), reviewed against the framework's QC checklists. Quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Code follows the `coding-conventions` skill for Python and the `clean-architecture` layering; source comments are written for Doxygen.

## Problem Statement

- The course gives the solution as notebook cells in Google Colab; there is no tested, structured, reusable version of it.
- A course participant who wants to compare solutions has to copy cells by hand, with no instructions to run them locally and no tests to prove the numbers.
- A GitHub visitor looking for ideas finds no explanation of what each step teaches.

## Business Opportunity

A clear, runnable repository with the assignment's function names, screenshots for each lecture step and a three-language wiki makes the exercise easy to study, compare and reuse. It also builds the participant's habits of working with a virtual environment, pytest, a pyproject file and a plan-first workflow.

## Objectives

1. Deliver the six lecture steps of Day 80 (591 to 596) as Python code in `src/`, covering data exploration, yearly and monthly births and deaths, the clinic split, the handwashing effect, histograms with a Kernel Density Estimate (KDE), and the p-value test.
2. Provide pytest tests in `tests/` that verify every number the lectures state (for example about 7.08 % deaths in the 1840s and about 267 births and 22.47 deaths per month).
3. Provide a Jupyter notebook that runs the same steps.
4. Document how to create and use a local `.venv` and how to run the project and its tests, on Linux and Windows.
5. Provide a README and a wiki in English, Danish and Bahasa Malaysia, with a screenshot for each lecture step and an explanation of what the step taught.
6. Publish the repository with a description and topics, one reviewed pull request per milestone.

## Scope

### In Scope

- Python 3.13 or newer, `venv`, `pyproject.toml`, Python `.gitignore`, `constants.py`, Doxygen comments and a `Doxyfile`.
- The two comma-separated values (CSV) data files and the notebook from the lecture resources (used as provided by the course, for personal study).
- Code for lectures 591 to 596, pytest tests, a Jupyter notebook.
- README from the framework template; wiki pages (en, da, ms) including a Getting Started page with Linux and Windows guides, modelled on the Getting Started page of project 074.
- Static analysis with opengrep before each push.
- Repository description and topics on the Gitea host.

### Out of Scope

- Any other course day.
- A graphical or web user interface.
- Runtime dependencies beyond what the analysis needs (pandas, NumPy, Matplotlib, SciPy).
- Publishing to PyPI.

## Expected Benefits

### Tangible Benefits

- A repository that runs from a clean clone with documented commands.
- Tests that fail if a lecture number changes.
- Screenshots and wiki pages for each of the six lecture steps.

### Intangible Benefits

- Understanding of how data and a significance test make an argument (the Semmelweis story).
- Practice with a structured, reviewed workflow.
- A reusable template for the next course-day repositories.

## Strategic Alignment

The repository is one of the participant's 100 Days of Code projects. It supports the aim of keeping each day's work readable and comparable for other course participants and visible as a portfolio on GitHub.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps implemented | 6 of 6 (591 to 596) | Each step has code and a wiki page |
| 2 | Tests pass | 100 % of tests pass on Python 3.13 | `pytest` exits 0 |
| 3 | Lecture numbers reproduced | All stated figures match | Tests assert them |
| 4 | Wiki languages | 3 (en, da, ms), same page set | Page list per language |
| 5 | Screenshots | At least 1 per lecture step in README and wiki | Image count |
| 6 | Run from clean clone | Documented commands work on Windows and Linux | Getting Started guides followed |
| 7 | Static analysis | 0 opengrep findings left unaddressed before each push | opengrep report |
| 8 | Runtime dependencies | Only the analysis libraries | `pyproject.toml` review |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Lecture resources cannot be downloaded | Data and notebook missing | Stop and report; the user supplies the files |
| Course data is copyrighted | Redistribution problem | Keep the repository for personal study; state the source and rights in the README |
| Screenshots need a signed-in Udemy session | Capture fails | Use the user's Chrome session; capture only the lecture view |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set checked before each review |
| Plotting tests are slow or flaky | CI red | Use the non-interactive Agg backend and assert on data, not pixels |
| Token leak | Credential exposure | Tokens stay in `.env`, which is git-ignored and never read by project code |

## Assumptions

- The user is the Product Owner and developer (S01); in autonomous mode the AI acts as reviewer stand-in for S01 and records it.
- The six Udemy lectures stay available in the user's Chrome session.
- The git host accepts the tokens in `.env` for issues, repository, wiki and release work.
- The PO language is English and the domain is IT.

## Constraints

- Python 3.13 or newer; `venv`; pytest; `pyproject.toml`; constants in `constants.py`.
- Folders `src/`, `tests/` and `docs/`.
- Nothing under `src/` or `tests/` before an accepted milestone with a `Go` review.
- Tokens are used only from `.env` for personal use, never imported or tested by the project.
- No GUI test on the host desktop.

## Cost–Benefit Assessment

Qualitative; the project is a personal learning exercise with no revenue, so a numeric model would add nothing.

| Costs | Benefits |
| --- | --- |
| The participant's time for six lecture steps, tests and a three-language wiki | A runnable, tested, documented portfolio repository and a reusable workflow |
| Review effort per milestone | Readable code for fellow course participants |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the goal, builds and reviews the work |
| S02 | Reads and runs the code and compares solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the lecture steps are well defined and the result is useful to all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md

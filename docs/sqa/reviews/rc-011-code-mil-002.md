# SQA Review Record RC-011

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [53dd280] |

---

## Artifact Under Review

- Instance reviewed: source code of MIL-002 on branch `mil-002-lecture-592` (loaders, exploration helpers, 7.08 percent result, twin-axis chart, tests, notebook section, step 2 picture and wiki pages in en, da and ms)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`; the code was written under the python-developer agent rules)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff (pycodestyle naming rules N) passes; names are snake_case / UPPER_SNAKE / PascalCase. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names come from the assignment (births, deaths, pct_deaths, before_washing, after_washing). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass with no suppressions except the documented E402 after the Agg backend call. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every signature is annotated, `-> None` included. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare or swallowed exceptions. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | Files are opened through `resources.as_file` context managers. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen docstrings (@brief, @param, @return) on every public module and function. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `logging` is used; no secrets or personal data are logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | N-A by ADR-0001: no Design Class Diagram exists; functions implement the milestone tasks directly. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | pytest tests named for the behaviour; no network; no order dependence; Agg backend. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | mypy strict was not run; only ruff is configured. Optional. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dependencies are declared in pyproject.toml with minimum versions; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Names, dates, colours and limits live in constants.py only. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports no I/O or chart code; infrastructure and presentation import domain and constants. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Small pure functions; one reason to change per module. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | src/semmelweis/{domain,infrastructure,presentation}; no application layer because there are no use cases (ADR-0001); tests/unit. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English names with letters, digits, `_` and `.` only. |

## Overall Verdict

Go — every applicable criterion of [QC-PY-001] is Pass or N-A. The review is by the author's stand-in and is not independent; S01 can challenge it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-12 |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[53dd280]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/commit/53dd280596c1b871723825bc6124ff18f4ea9124

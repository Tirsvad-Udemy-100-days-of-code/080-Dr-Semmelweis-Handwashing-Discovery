**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer and Git. Runtime dependencies: `pandas`, `numpy`, `matplotlib` and `scipy`. Nothing else is needed to run the analysis.

## Windows (PowerShell)

Create and use a local `.venv`:

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery.git
cd 080-Dr-Semmelweis-Handwashing-Discovery
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, run `Set-ExecutionPolicy -Scope Process RemoteSigned` first; it only applies to the current window.

## Linux and macOS (bash)

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery.git
cd 080-Dr-Semmelweis-Handwashing-Discovery
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run, test and open the notebook

The commands are the same on every system once the `.venv` is active:

```bash
python -m pytest
python -m ruff check src tests
python -m pip install -e ".[notebook]"
jupyter lab notebooks
```

`jupyter lab` needs the `notebook` extra, which also installs `plotly` and `seaborn` for the course's own notebook. The project code itself does not use them.

## Check the code with opengrep

Run opengrep before every push. On Windows the program is `~\.opengrep\cli\latest\opengrep.exe`; on Linux it is `~/.opengrep/cli/latest/opengrep`:

```bash
~/.opengrep/cli/latest/opengrep scan --config p/python src tests
```

Fix every finding before you push.

## Build the Doxygen documentation (optional)

```bash
doxygen Doxyfile
```

The pages are written to `docs/doxygen/html`.

**What you gain:** a repeatable set-up (one virtual environment per project), a package installed in editable mode, tests that prove each answer, and a static check before you share your code.

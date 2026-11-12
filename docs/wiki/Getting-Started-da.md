[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Krav: Python 3.13 eller nyere og Git. Afhængigheder ved kørsel: `pandas`, `numpy`, `matplotlib` og `scipy`. Der skal ikke mere til for at køre analysen.

## Windows (PowerShell)

Opret og brug et lokalt `.venv`:

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery.git
cd 080-Dr-Semmelweis-Handwashing-Discovery
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Hvis PowerShell afviser aktiveringsscriptet, så kør først `Set-ExecutionPolicy -Scope Process RemoteSigned`; det gælder kun for det aktuelle vindue.

## Linux og macOS (bash)

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery.git
cd 080-Dr-Semmelweis-Handwashing-Discovery
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Kør, test og åbn notebook

Kommandoerne er ens på alle systemer, når `.venv` er aktivt:

```bash
python -m pytest
python -m ruff check src tests
python -m pip install -e ".[notebook]"
jupyter lab notebooks
```

`jupyter lab` kræver `notebook`-tilvalget, som også installerer `plotly` og `seaborn` til kursets egen notebook. Selve projektets kode bruger dem ikke.

## Kontrollér koden med opengrep

Kør opengrep før hvert push. På Windows er programmet `~\.opengrep\cli\latest\opengrep.exe`; på Linux er det `~/.opengrep/cli/latest/opengrep`:

```bash
~/.opengrep/cli/latest/opengrep scan --config p/python src tests
```

Ret alle fund, før du pusher.

## Byg Doxygen-dokumentationen (valgfrit)

```bash
doxygen Doxyfile
```

Siderne skrives til `docs/doxygen/html`.

**Det får du ud af det:** en gentagelig opsætning (ét virtuelt miljø pr. projekt), en pakke installeret i redigerbar tilstand, tests der beviser hvert svar, og en statisk kontrol, før du deler din kode.

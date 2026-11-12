[English](Step-2-Data-Exploration) · **Dansk** · [Bahasa Malaysia](Step-2-Data-Exploration-ms)

# Trin 2: Indledende dataudforskning

**Spørgsmål:** Hvad er der i dataene, er de rene, og hvor farligt var det at føde i Wien i 1840'erne?

![Trin 2: månedlige fødsler og dødsfald på to akser](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-2-data-exploration.png)

## Hvad koden gør

- `load_yearly` og `load_monthly` læser de to CSV-filer; den månedlige indlæser fortolker kolonnen `date`, så der ikke skal konverteres senere.
- `table_shape`, `column_names`, `has_nan_values` og `has_duplicates` besvarer den første udfordring: den årlige tabel har 12 rækker og 4 kolonner, den månedlige 98 rækker og 3 kolonner, og der er ingen `NaN`-værdier og ingen dubletter.
- `average_births_per_month` og `average_deaths_per_month` giver omkring 267 fødsler og 22,47 dødsfald pr. måned.
- `percentage_of_women_dying` dividerer de samlede dødsfald med de samlede fødsler i de årlige data: omkring 7,08 %, sammenlignet med 0,018 % i USA i 2013.
- `births_and_deaths_chart` tegner fødsler og dødsfald på to y-akser med år og måneder som skalastreger, et gitter, linjerne `skyblue` og `crimson`, en stiplet dødslinje og linjebredde 3 og 2. I slutningen af 1840'erne falder antallet af dødsfald kraftigt, mens antallet af fødsler ikke gør.

## Det fik du ud af det

- `.shape`, `.head()`, `.tail()`, `.info()`, `.describe()`, `.isna()` og `.duplicated()` giver et første billede af enhver DataFrame.
- En procentdel er en sum divideret med en sum, gange 100.
- `.twinx()` lader to dataserier med forskellig skala dele én x-akse, og `MonthLocator` og `YearLocator` gør en tidsakse læsbar.

Forrige: [Step-1-Goals-da](Step-1-Goals-da)

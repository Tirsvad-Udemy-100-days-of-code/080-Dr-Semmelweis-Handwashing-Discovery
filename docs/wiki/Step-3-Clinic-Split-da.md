[English](Step-3-Clinic-Split) · **Dansk** · [Bahasa Malaysia](Step-3-Clinic-Split-ms)

# Trin 3: De årlige data opdelt efter klinik

**Spørgsmål:** Hvilken af de to klinikker var travlest, og hvilken var farligst?

![Trin 3: fødsler, dødsfald og andelen af dødsfald pr. klinik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-3-clinic-split.png)

## Hvad koden gør

- `births_by_clinic_chart` og `deaths_by_clinic_chart` tegner én linje pr. klinik, så klinikkerne kan sammenlignes år for år. Klinik 1 er den største (20.042 fødsler mod 17.791 i klinik 2), og begge klinikker fik flere patienter over tid. Det højeste antal årlige dødsfald var 518 i klinik 1 (1842) og 202 i klinik 2 (1842).
- `add_pct_deaths` tilføjer kolonnen `pct_deaths`, dødsfald divideret med fødsler for hver række, til en kopi af den årlige tabel. Det er uretfærdigt kun at tælle dødsfald, når klinikkerne har forskellig størrelse; andelen sammenligner ens med ens.
- `average_death_rate` dividerer en kliniks samlede dødsfald med dens samlede fødsler: omkring 9,92 % for klinik 1 og omkring 3,88 % for klinik 2.
- `pct_deaths_by_clinic_chart` viser andelen pr. år. Klinik 1 har den højeste andel af dødsfald i hvert eneste år, og det er gåden, Dr Semmelweis ville forklare.

## Det fik du ud af det

- At udvælge rækkerne for en gruppe med en betingelse, for eksempel `df[df.clinic == "clinic 1"]`.
- En afledt kolonne (`pct_deaths`) gør rå tal til en rate, der kan sammenlignes.
- En rate for en hel gruppe er summen af dens dødsfald divideret med summen af dens fødsler, ikke gennemsnittet af de årlige rater.
- Én linje pr. gruppe med en signaturforklaring er den enkleste måde at sammenligne grupper over tid.

Forrige: [Step-2-Data-Exploration-da](Step-2-Data-Exploration-da)

[English](Step-4-Handwashing-Effect) · **Dansk** · [Bahasa Malaysia](Step-4-Handwashing-Effect-ms)

# Trin 4: Effekten af håndvask

**Spørgsmål:** Nedsatte det andelen af kvinder, der døde, at lægerne skulle vaske hænder i juni 1847?

![Trin 4: månedlig andel af dødsfald med håndvaskperioden fremhævet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-4-handwashing-effect.png)

## Hvad koden gør

- `add_pct_deaths_monthly` tilføjer kolonnen `pct_deaths`, dødsfald divideret med fødsler for hver måned, til en kopi af den månedlige tabel.
- `split_before_after` bruger konstanten `HANDWASHING_START` (1. juni 1847) til at dele de månedlige data i månederne før og månederne efter, at håndvask blev obligatorisk.
- `average_rate_before_after` dividerer periodens samlede dødsfald med dens samlede fødsler: omkring 10,53 % før og omkring 2,15 % efter. `mean_of_rates_before_after` tager i stedet gennemsnittet af de månedlige rater og giver omkring 10,5 % og omkring 2,11 %.
- `improvement_factor` dividerer raten før med raten efter: håndvask skar andelen af dødsfald ned med en faktor på omkring 4,9.
- `rolling_average` udjævner den støjende månedlige rate med et vindue på 6 måneder, og `handwashing_chart` tegner den månedlige rate, det glidende gennemsnit og de to perioder i forskellige farver med en signaturforklaring.

## Det fik du ud af det

- At tilføje en afledt kolonne til en tidsserie og dele en DataFrame på en dato med en betingelse.
- En rate for en periode er summen af dødsfald divideret med summen af fødsler; gennemsnittet af de månedlige rater ligger tæt på, men er ikke det samme.
- Et glidende gennemsnit viser tendensen gennem støjende månedsværdier.
- At farve de to perioder forskelligt og tilføje en signaturforklaring gør en før-og-efter-sammenligning læsbar med et blik.

Forrige: [Step-3-Clinic-Split-da](Step-3-Clinic-Split-da) · Næste: [Step-5-Distributions-da](Step-5-Distributions-da)

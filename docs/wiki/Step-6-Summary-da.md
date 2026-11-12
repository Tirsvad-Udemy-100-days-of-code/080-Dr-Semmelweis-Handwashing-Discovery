[English](Step-6-Summary) · **Dansk** · [Bahasa Malaysia](Step-6-Summary-ms)

# Trin 6: Læringspunkter og opsummering

**Spørgsmål:** Hvad lærte dag 80 dig, og hvad siger data om håndvask?

![Trin 6: hovedresultaterne og den månedlige dødelighed med glidende gennemsnit](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-6-summary.png)

## Hvad koden gør

`step_6_summary` tegner hovedresultaterne ud fra de samme domænefunktioner som de tidligere trin, uden at noget tal er skrevet ind i hånden: dødeligheden før håndvask (omkring 10,53 %) og efter (omkring 2,15 %), forbedringsfaktoren (omkring 4,9 gange lavere), t-værdien (omkring 5,51), p-værdien (omkring 0,0000003) og at resultatet er signifikant på 1 %-niveauet. Ved siden af tegner den den månedlige dødelighed med det glidende gennemsnit over 6 måneder og datoen, hvor håndvask begyndte.

## Det fik du ud af det

- **Data først:** `.shape`, `.head()`, `.isna()` og `.duplicated()` viser, hvad data indeholder, før nogen analyse (trin 2).
- **Fair sammenligninger:** en rate som andelen af dødsfald sammenligner klinikker og perioder af forskellig størrelse bedre end antal (trin 3 og 4).
- **Tidsserier:** et glidende gennemsnit viser tendensen gennem støjende måneder, og farve, en markørlinje og en signaturforklaring viser, hvor ændringen skete (trin 4).
- **Fordelinger:** `np.where` laver en gruppekolonne; boksplot, histogrammer og et kerneltæthedsestimat viser de samme grupper på tre måder (trin 5).
- **Statistisk signifikans:** en t-test og dens p-værdi viser, om en forskel er større end tilfældigheder; her er p langt under 0,01, så faldet efter håndvask er reelt (trin 5).
- **Konklusion:** efter håndvaskreglen i juni 1847 faldt andelen af kvinder, der døde, fra omkring 10,5 % til omkring 2,1 %, og data siger, at det ikke er tilfældigt.

Forrige: [Step-5-Distributions-da](Step-5-Distributions-da)

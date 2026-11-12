[English](Step-5-Distributions) · **Dansk** · [Bahasa Malaysia](Step-5-Distributions-ms)

# Trin 5: Fordelinger og statistisk signifikans

**Spørgsmål:** Er faldet i dødeligheden efter håndvask reelt, eller kan det være tilfældigt?

![Trin 5: boksplot, histogram og kerneltæthedsestimat af den månedlige dødelighed med og uden håndvask](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-5-distributions.png)

## Hvad koden gør

- `add_washing_hands` tilføjer den boolske kolonne `washing_hands`, sand for månederne fra `HANDWASHING_START` og frem, til en kopi af den månedlige tabel. `group_means` giver den gennemsnitlige månedlige rate for hver gruppe: omkring 10,5 % uden og omkring 2,11 % med håndvask.
- `box_plot_chart` viser de to grupper som boksplot: medianen, kvartilerne og afvigerne. Både den typiske rate og spredningen er lavere efter håndvask.
- `histogram_overlay_chart` tegner de to histogrammer oven på hinanden med 30 fælles intervaller, gennemsigtige søjler og procent af måneder på y-aksen, så grupper af forskellig størrelse kan sammenlignes.
- `kde_chart` og `kde_curve` udjævner hvert histogram til et kerneltæthedsestimat (KDE). Kurven afskæres ved gruppens mindste og største værdi, fordi en dødelighed ikke kan være negativ.
- `two_sample_t_test` kører SciPys `ttest_ind` på de to grupper og returnerer t-værdien og p-værdien: t på omkring 5,51 og p på omkring 0,0000003. `is_significant` sammenligner p-værdien med niveauet 0,01, så forskellen er signifikant på 99 %-niveauet.

## Det fik du ud af det

- `np.where` eller en almindelig sammenligning gør en datobetingelse til en boolsk kolonne, der grupperer data.
- Et boksplot, et histogram og et KDE viser de samme data på tre måder: sammenfatning, antal og form.
- En t-test spørger, om forskellen mellem to gennemsnit er større, end tilfældigheder kan give; en lille p-værdi siger, at den er, og 0,0000003 er langt under 0,01.
- `scipy.stats.ttest_ind` antager som standard ens varians (Students test), hvilket forelæsningen bruger; Welchs test med `equal_var=False` giver et andet tal.

Forrige: [Step-4-Handwashing-Effect-da](Step-4-Handwashing-Effect-da) · Næste: [Step-6-Summary-da](Step-6-Summary-da)

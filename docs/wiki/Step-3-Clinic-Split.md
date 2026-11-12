**English** · [Dansk](Step-3-Clinic-Split-da) · [Bahasa Malaysia](Step-3-Clinic-Split-ms)

# Step 3: The yearly data split by clinic

**Question:** Which of the two clinics was busier, and which one was more dangerous?

![Step 3: births, deaths and the proportion of deaths per clinic](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-3-clinic-split.png)

## What the code does

- `births_by_clinic_chart` and `deaths_by_clinic_chart` draw one line per clinic, so the clinics can be compared year by year. Clinic 1 is the bigger one (20,042 births against 17,791 in clinic 2), and both clinics had more patients over time. The highest number of yearly deaths was 518 in clinic 1 (1842) and 202 in clinic 2 (1842).
- `add_pct_deaths` adds the column `pct_deaths`, the deaths divided by the births of each row, to a copy of the yearly table. Counting deaths alone is unfair when the clinics have different sizes; the proportion compares like with like.
- `average_death_rate` divides the total deaths of a clinic by its total births: about 9.92 % for clinic 1 and about 3.88 % for clinic 2.
- `pct_deaths_by_clinic_chart` shows the proportion per year. Clinic 1 has the higher proportion of deaths in every year, which is the puzzle Dr Semmelweis wanted to explain.

## What you gained

- Selecting the rows of a group with a condition, for example `df[df.clinic == "clinic 1"]`.
- A derived column (`pct_deaths`) turns raw counts into a rate that can be compared.
- A rate for a whole group is the sum of its deaths divided by the sum of its births, not the average of the yearly rates.
- One line per group, with a legend, is the simplest way to compare groups over time.

Previous: [Step-2-Data-Exploration](Step-2-Data-Exploration)

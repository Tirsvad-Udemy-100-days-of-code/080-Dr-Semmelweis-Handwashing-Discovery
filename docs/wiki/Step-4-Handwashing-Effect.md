**English** · [Dansk](Step-4-Handwashing-Effect-da) · [Bahasa Malaysia](Step-4-Handwashing-Effect-ms)

# Step 4: The effect of handwashing

**Question:** Did making doctors wash their hands in June 1847 lower the proportion of women who died?

![Step 4: monthly proportion of deaths with the handwashing period highlighted](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-4-handwashing-effect.png)

## What the code does

- `add_pct_deaths_monthly` adds the column `pct_deaths`, the deaths divided by the births of each month, to a copy of the monthly table.
- `split_before_after` uses the constant `HANDWASHING_START` (1 June 1847) to cut the monthly data into the months before and the months after handwashing became mandatory.
- `average_rate_before_after` divides the total deaths of each period by its total births: about 10.53 % before and about 2.15 % after. `mean_of_rates_before_after` averages the monthly rates instead and gives about 10.5 % and about 2.11 %.
- `improvement_factor` divides the rate before by the rate after: handwashing cut the proportion of deaths by a factor of about 4.9.
- `rolling_average` smooths the noisy monthly rate with a 6 month window, and `handwashing_chart` draws the monthly rate, the rolling average and the two periods in different colours, with a legend.

## What you gained

- Adding a derived column to a time series, and splitting a DataFrame on a date with a condition.
- A rate for a period is the sum of its deaths divided by the sum of its births; the mean of monthly rates is close, but not the same.
- A rolling average shows the trend through noisy monthly values.
- Colouring the two periods differently and adding a legend makes a before and after comparison readable at a glance.

Previous: [Step-3-Clinic-Split](Step-3-Clinic-Split) · Next: [Step-5-Distributions](Step-5-Distributions)

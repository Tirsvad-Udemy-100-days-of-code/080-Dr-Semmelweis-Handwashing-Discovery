**English** · [Dansk](Step-6-Summary-da) · [Bahasa Malaysia](Step-6-Summary-ms)

# Step 6: Learning points and summary

**Question:** What did Day 80 teach, and what does the data say about handwashing?

![Step 6: the headline results and the monthly death rate with its rolling average](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-6-summary.png)

## What the code does

`step_6_summary` draws the headline results from the same domain functions as the earlier steps, with no number typed in by hand: the death rate before handwashing (about 10.53 %) and after (about 2.15 %), the improvement factor (about 4.9 times lower), the t statistic (about 5.51), the p-value (about 0.0000003) and that the result is significant at the 1 % level. Next to them it draws the monthly death rate with its 6 month rolling average and the date handwashing began.

## What you gained

- **Data first:** `.shape`, `.head()`, `.isna()` and `.duplicated()` show what the data holds before any analysis (step 2).
- **Fair comparisons:** a rate such as the proportion of deaths compares clinics and periods of different size better than counts do (steps 3 and 4).
- **Time series:** a rolling average shows the trend through noisy months, and colour, a marker line and a legend show where the change happened (step 4).
- **Distributions:** `np.where` makes a group column; box plots, histograms and a Kernel Density Estimate show the same groups in three ways (step 5).
- **Statistical significance:** a t-test and its p-value tell whether a difference is larger than chance; here p is far below 0.01, so the drop after handwashing is real (step 5).
- **Conclusion:** after the handwashing rule of June 1847 the proportion of women who died fell from about 10.5 % to about 2.1 %, and the data says it is not chance.

Previous: [Step-5-Distributions](Step-5-Distributions)

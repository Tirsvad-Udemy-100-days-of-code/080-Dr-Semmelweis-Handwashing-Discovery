**English** · [Dansk](Step-5-Distributions-da) · [Bahasa Malaysia](Step-5-Distributions-ms)

# Step 5: Distributions and statistical significance

**Question:** Is the drop in the death rate after handwashing real, or could it be chance?

![Step 5: box plot, histogram and kernel density estimate of the monthly death rate with and without handwashing](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-5-distributions.png)

## What the code does

- `add_washing_hands` adds the boolean column `washing_hands`, true for the months from `HANDWASHING_START` on, to a copy of the monthly table. `group_means` gives the mean monthly rate of each group: about 10.5 % without and about 2.11 % with handwashing.
- `box_plot_chart` shows the two groups as box plots: the median, the quartiles and the outliers. Both the typical rate and the spread are lower after handwashing.
- `histogram_overlay_chart` draws the two histograms on top of each other with 30 shared bins, transparent bars and percent of months on the y axis, so the groups of different size can be compared.
- `kde_chart` and `kde_curve` smooth each histogram into a Kernel Density Estimate. The curve is cut off at the smallest and the largest value of the group, because a death rate cannot be negative.
- `two_sample_t_test` runs SciPy's `ttest_ind` on the two groups and returns the t statistic and the p-value: t of about 5.51 and p of about 0.0000003. `is_significant` compares the p-value with the level 0.01, so the difference is significant at the 99 % level.

## What you gained

- `np.where` or a plain comparison turns a date condition into a boolean column that groups the data.
- A box plot, a histogram and a KDE show the same data in three ways: summary, counts and shape.
- A t-test asks whether the difference between two means is larger than chance would give; a small p-value says it is, and 0.0000003 is far below 0.01.
- `scipy.stats.ttest_ind` by default assumes equal variances (Student's test), which is what the lecture uses; Welch's test, with `equal_var=False`, gives a different number.

Previous: [Step-4-Handwashing-Effect](Step-4-Handwashing-Effect) · Next: [Step-6-Summary](Step-6-Summary)

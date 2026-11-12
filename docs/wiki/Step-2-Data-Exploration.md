**English** · [Dansk](Step-2-Data-Exploration-da) · [Bahasa Malaysia](Step-2-Data-Exploration-ms)

# Step 2: Preliminary data exploration

**Question:** What is in the data, is it clean, and how dangerous was childbirth in Vienna in the 1840s?

![Step 2: monthly births and deaths on twin axes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/080-Dr-Semmelweis-Handwashing-Discovery/raw/branch/main/docs/images/step-2-data-exploration.png)

## What the code does

- `load_yearly` and `load_monthly` read the two CSV files; the monthly loader parses the `date` column so no conversion is needed later.
- `table_shape`, `column_names`, `has_nan_values` and `has_duplicates` answer the first challenge: the yearly table has 12 rows and 4 columns, the monthly table 98 rows and 3 columns, there are no `NaN` values and no duplicates.
- `average_births_per_month` and `average_deaths_per_month` give about 267 births and 22.47 deaths per month.
- `percentage_of_women_dying` divides the total deaths by the total births of the yearly data: about 7.08 %, compared with 0.018 % in the United States in 2013.
- `births_and_deaths_chart` draws births and deaths on twin y axes with year and month tick marks, a grid, `skyblue` and `crimson` lines, a dashed deaths line and line widths 3 and 2. In the late 1840s the number of deaths falls sharply while the number of births does not.

## What you gained

- `.shape`, `.head()`, `.tail()`, `.info()`, `.describe()`, `.isna()` and `.duplicated()` give a first picture of any DataFrame.
- A percentage is a sum divided by a sum, times 100.
- `.twinx()` lets two series with different scales share one x axis, and `MonthLocator` and `YearLocator` make a time axis readable.

Previous: [Step-1-Goals](Step-1-Goals)

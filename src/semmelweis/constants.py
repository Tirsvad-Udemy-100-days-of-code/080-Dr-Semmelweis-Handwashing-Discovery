"""@brief Constants used by the Day 80 analysis.

@details Every file name, column name, date, colour and statistical limit that
the lectures use is defined here once, so no module repeats a magic value.
"""

from typing import Final

## @name Data files
## @{
DATA_PACKAGE: Final[str] = "semmelweis.data"
YEARLY_FILE: Final[str] = "annual_deaths_by_clinic.csv"
MONTHLY_FILE: Final[str] = "monthly_deaths.csv"
## @}

## @name Column names
## @{
COL_YEAR: Final[str] = "year"
COL_DATE: Final[str] = "date"
COL_BIRTHS: Final[str] = "births"
COL_DEATHS: Final[str] = "deaths"
COL_CLINIC: Final[str] = "clinic"
COL_PCT_DEATHS: Final[str] = "pct_deaths"
COL_WASHING_HANDS: Final[str] = "washing_hands"
## @}

## @name Clinics
## @{
CLINIC_1: Final[str] = "clinic 1"
CLINIC_2: Final[str] = "clinic 2"
## @}

## @name Handwashing study
## @{
HANDWASHING_START: Final[str] = "1847-06-01"
ROLLING_WINDOW_MONTHS: Final[int] = 6
SIGNIFICANCE_LEVEL: Final[float] = 0.01
LABEL_YES: Final[str] = "Yes"
LABEL_NO: Final[str] = "No"
## @}

## @name Chart style
## @{
FIGURE_SIZE: Final[tuple[int, int]] = (14, 8)
FIGURE_DPI: Final[int] = 100
COLOR_BIRTHS: Final[str] = "skyblue"
COLOR_DEATHS: Final[str] = "crimson"
LINEWIDTH_BIRTHS: Final[int] = 3
LINEWIDTH_DEATHS: Final[int] = 2
LINESTYLE_DEATHS: Final[str] = "--"
GRID_COLOR: Final[str] = "grey"
GRID_LINESTYLE: Final[str] = "--"
CHART_TITLE: Final[str] = "Total Number of Monthly Births and Deaths"
CHART_TITLE_FONT_SIZE: Final[int] = 18
AXIS_LABEL_FONT_SIZE: Final[int] = 18
TICK_FONT_SIZE: Final[int] = 14
TICK_ROTATION: Final[int] = 45
LABEL_BIRTHS: Final[str] = "Births"
LABEL_DEATHS: Final[str] = "Deaths"
YEAR_FORMAT: Final[str] = "%Y"
## @}

## @name Exploration
## @{
PERCENT: Final[int] = 100
## @}

## @name Step pictures
## @{
IMAGES_DIR: Final[tuple[str, str]] = ("docs", "images")
PREVIEW_ROWS: Final[int] = 6
OVERVIEW_FIGURE_SIZE: Final[tuple[float, float]] = (13.0, 4.5)
OVERVIEW_TITLE: Final[str] = "Day 80: Vienna General Hospital, 1841 to 1849"
SUPTITLE_FONT_SIZE: Final[int] = 16
TABLE_TITLE_FONT_SIZE: Final[int] = 14
TABLE_TITLE_PAD: Final[int] = 12
TABLE_FONT_SIZE: Final[int] = 11
TABLE_ROW_SCALE: Final[float] = 1.6
STEP_1_NAME: Final[str] = "step-1-goals"
STEP_2_NAME: Final[str] = "step-2-data-exploration"
## @}

## @name Clinic split (lecture 593)
## @{
CLINICS: Final[tuple[str, str]] = (CLINIC_1, CLINIC_2)
CLINIC_COLORS: Final[dict[str, str]] = {CLINIC_1: "crimson", CLINIC_2: "steelblue"}
CLINIC_LINEWIDTH: Final[int] = 3
LABEL_YEAR: Final[str] = "Year"
TITLE_BIRTHS_BY_CLINIC: Final[str] = "Total Yearly Births by Clinic"
TITLE_DEATHS_BY_CLINIC: Final[str] = "Total Yearly Deaths by Clinic"
TITLE_PCT_DEATHS_BY_CLINIC: Final[str] = "Proportion of Yearly Deaths by Clinic"
CLINIC_OVERVIEW_FIGURE_SIZE: Final[tuple[float, float]] = (15.0, 4.8)
CLINIC_OVERVIEW_TITLE_FONT_SIZE: Final[int] = 12
CLINIC_LEGEND_FONT_SIZE: Final[int] = 10
STEP_3_NAME: Final[str] = "step-3-clinic-split"
## @}

## @name Handwashing effect (lecture 594)
## @{
COL_ROLLING_PCT_DEATHS: Final[str] = "rolling_pct_deaths"
TITLE_HANDWASHING: Final[str] = (
    "Percentage of Monthly Deaths over Time (before and after handwashing)"
)
LABEL_PCT_DEATHS: Final[str] = "Percentage of Monthly Deaths"
LABEL_MONTH: Final[str] = "Month"
LABEL_BEFORE_HANDWASHING: Final[str] = "Before handwashing"
LABEL_AFTER_HANDWASHING: Final[str] = "After handwashing"
LABEL_ROLLING_AVERAGE: Final[str] = "6-month rolling average"
LABEL_HANDWASHING_START: Final[str] = "Handwashing made mandatory"
COLOR_BEFORE_HANDWASHING: Final[str] = "crimson"
COLOR_AFTER_HANDWASHING: Final[str] = "steelblue"
COLOR_ROLLING_AVERAGE: Final[str] = "black"
COLOR_HANDWASHING_START: Final[str] = "grey"
LINEWIDTH_PCT_DEATHS: Final[int] = 2
LINEWIDTH_ROLLING_AVERAGE: Final[int] = 3
LINESTYLE_ROLLING_AVERAGE: Final[str] = "--"
LINESTYLE_HANDWASHING_START: Final[str] = ":"
HANDWASHING_LEGEND_FONT_SIZE: Final[int] = 14
STEP_4_NAME: Final[str] = "step-4-handwashing-effect"
## @}

## @name Distributions and significance (lecture 595)
## @{
HISTOGRAM_BINS: Final[int] = 30
HISTOGRAM_ALPHA: Final[float] = 0.6
KDE_POINTS: Final[int] = 200
KDE_FILL_ALPHA: Final[float] = 0.25
KDE_LINEWIDTH: Final[int] = 3
TITLE_BOX_PLOT: Final[str] = "Monthly Death Rate With and Without Handwashing"
TITLE_HISTOGRAM: Final[str] = "Histogram of Monthly Death Rates (percent of months)"
TITLE_KDE: Final[str] = "Kernel Density Estimate of Monthly Death Rates"
LABEL_WASHING_HANDS: Final[str] = "Washing Hands?"
LABEL_PERCENT_OF_MONTHS: Final[str] = "Percent of months"
LABEL_DENSITY: Final[str] = "Probability density"
LABEL_WITHOUT_HANDWASHING: Final[str] = "Without handwashing"
LABEL_WITH_HANDWASHING: Final[str] = "With handwashing"
DISTRIBUTION_LEGEND_FONT_SIZE: Final[int] = 11
DISTRIBUTION_FIGURE_SIZE: Final[tuple[float, float]] = (15.0, 5.0)
DISTRIBUTION_TITLE_FONT_SIZE: Final[int] = 12
BOX_PLOT_WIDTH: Final[float] = 0.5
STEP_5_NAME: Final[str] = "step-5-distributions"
## @}

## @name Learning points and summary (lecture 596)
## @{
SUMMARY_TITLE: Final[str] = "Day 80: Learning Points and Summary"
SUMMARY_FIGURE_SIZE: Final[tuple[float, float]] = (13.0, 5.0)
SUMMARY_WIDTH_RATIOS: Final[tuple[int, int]] = (5, 6)
SUMMARY_HEADING: Final[str] = "Headline results"
SUMMARY_CHART_TITLE: Final[str] = "Monthly death rate and 6-month rolling average"
SUMMARY_TEXT_FONT_SIZE: Final[int] = 14
SUMMARY_HEADING_FONT_SIZE: Final[int] = 15
SUMMARY_TEXT_X: Final[float] = 0.02
SUMMARY_HEADING_Y: Final[float] = 0.95
SUMMARY_TEXT_Y: Final[float] = 0.82
SUMMARY_LINE_SPACING: Final[float] = 1.9
SUMMARY_BOX_COLOR: Final[str] = "whitesmoke"
SUMMARY_CHART_FONT_SIZE: Final[int] = 11
SUMMARY_LINE_BEFORE: Final[str] = "Death rate before handwashing: {:.2f}%"
SUMMARY_LINE_AFTER: Final[str] = "Death rate after handwashing: {:.2f}%"
SUMMARY_LINE_FACTOR: Final[str] = "Improvement factor: {:.1f}x lower"
SUMMARY_LINE_T_STATISTIC: Final[str] = "t statistic: {:.2f}"
SUMMARY_LINE_P_VALUE: Final[str] = "p-value: {:.2e}"
SUMMARY_LINE_SIGNIFICANT: Final[str] = "Significant at the {:.0%} level: {}"
STEP_6_NAME: Final[str] = "step-6-summary"
## @}

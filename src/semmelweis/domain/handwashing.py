"""@brief Questions asked about the effect of handwashing (lecture 594)."""

import pandas as pd

from semmelweis import constants


def add_pct_deaths_monthly(monthly: pd.DataFrame) -> pd.DataFrame:
    """@brief Add the proportion of births that ended in a death.

    @param monthly The monthly table; it is not changed.
    @return A copy with the column pct_deaths (deaths divided by births).
    """
    result = monthly.copy()
    result[constants.COL_PCT_DEATHS] = (
        result[constants.COL_DEATHS] / result[constants.COL_BIRTHS]
    )
    return result


def split_before_after(
    monthly: pd.DataFrame, start: str = constants.HANDWASHING_START
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """@brief Split the monthly table at the date handwashing became mandatory.

    @param monthly The monthly table.
    @param start First day of the period after handwashing began.
    @return The rows before start and the rows from start on.
    """
    boundary = pd.Timestamp(start)
    is_before = monthly[constants.COL_DATE] < boundary
    return monthly[is_before], monthly[~is_before]


def _sum_rate(rows: pd.DataFrame) -> float:
    """@brief Total deaths divided by total births of some rows, in percent.

    @param rows Rows of the monthly table.
    @return The death rate in percent.
    """
    deaths = rows[constants.COL_DEATHS].sum()
    births = rows[constants.COL_BIRTHS].sum()
    return float(deaths / births * constants.PERCENT)


def average_rate_before_after(
    monthly: pd.DataFrame, start: str = constants.HANDWASHING_START
) -> tuple[float, float]:
    """@brief Death rate of each period from summed deaths and births.

    @param monthly The monthly table.
    @param start First day of the period after handwashing began.
    @return The rate before and the rate after, in percent.
    """
    before, after = split_before_after(monthly, start)
    return _sum_rate(before), _sum_rate(after)


def mean_of_rates_before_after(
    monthly: pd.DataFrame, start: str = constants.HANDWASHING_START
) -> tuple[float, float]:
    """@brief Mean of the monthly death rates of each period.

    @param monthly The monthly table; pct_deaths is computed when missing.
    @param start First day of the period after handwashing began.
    @return The mean before and the mean after, in percent.
    """
    data = (
        monthly
        if constants.COL_PCT_DEATHS in monthly.columns
        else add_pct_deaths_monthly(monthly)
    )
    before, after = split_before_after(data, start)
    return (
        float(before[constants.COL_PCT_DEATHS].mean() * constants.PERCENT),
        float(after[constants.COL_PCT_DEATHS].mean() * constants.PERCENT),
    )


def improvement_factor(before_rate: float, after_rate: float) -> float:
    """@brief How many times lower the death rate became.

    @param before_rate Death rate before handwashing.
    @param after_rate Death rate after handwashing.
    @return before_rate divided by after_rate.
    """
    return before_rate / after_rate


def rolling_average(
    monthly: pd.DataFrame, window: int = constants.ROLLING_WINDOW_MONTHS
) -> pd.DataFrame:
    """@brief Add the rolling average of the monthly proportion of deaths.

    @param monthly The monthly table; pct_deaths is computed when missing.
    @param window Number of months averaged.
    @return A copy with the column rolling_pct_deaths; the first window - 1
        rows are NaN.
    """
    result = (
        monthly.copy()
        if constants.COL_PCT_DEATHS in monthly.columns
        else add_pct_deaths_monthly(monthly)
    )
    result[constants.COL_ROLLING_PCT_DEATHS] = (
        result[constants.COL_PCT_DEATHS].rolling(window=window).mean()
    )
    return result

"""@brief Questions asked about the raw data in the preliminary exploration."""

import pandas as pd

from semmelweis import constants


def table_shape(frame: pd.DataFrame) -> tuple[int, int]:
    """@brief Count the rows and columns of a table.

    @param frame The table.
    @return A pair (rows, columns).
    """
    rows, columns = frame.shape
    return rows, columns


def column_names(frame: pd.DataFrame) -> list[str]:
    """@brief List the column names of a table.

    @param frame The table.
    @return The names in column order.
    """
    return [str(name) for name in frame.columns]


def years_covered(yearly: pd.DataFrame) -> list[int]:
    """@brief List the years present in the yearly table.

    @param yearly The yearly table.
    @return The distinct years in ascending order.
    """
    return sorted(int(year) for year in yearly[constants.COL_YEAR].unique())


def has_nan_values(frame: pd.DataFrame) -> bool:
    """@brief Tell whether any cell of the table is missing.

    @param frame The table.
    @return True when at least one value is NaN.
    """
    return bool(frame.isna().values.any())


def has_duplicates(frame: pd.DataFrame) -> bool:
    """@brief Tell whether any row of the table repeats an earlier row.

    @param frame The table.
    @return True when at least one row is a duplicate.
    """
    return bool(frame.duplicated().any())


def average_births_per_month(monthly: pd.DataFrame) -> float:
    """@brief Average number of births per month.

    @param monthly The monthly table.
    @return The mean of the births column.
    """
    return float(monthly[constants.COL_BIRTHS].mean())


def average_deaths_per_month(monthly: pd.DataFrame) -> float:
    """@brief Average number of deaths per month.

    @param monthly The monthly table.
    @return The mean of the deaths column.
    """
    return float(monthly[constants.COL_DEATHS].mean())


def percentage_of_women_dying(yearly: pd.DataFrame) -> float:
    """@brief Share of births that ended in the death of the mother.

    @param yearly The yearly table.
    @return Total deaths divided by total births, in percent.
    """
    deaths = yearly[constants.COL_DEATHS].sum()
    births = yearly[constants.COL_BIRTHS].sum()
    return float(deaths / births * constants.PERCENT)

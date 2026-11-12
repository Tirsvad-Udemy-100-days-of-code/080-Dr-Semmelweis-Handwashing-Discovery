"""@brief Questions asked about the yearly data split by clinic (lecture 593)."""

import pandas as pd

from semmelweis import constants


def clinic_rows(yearly: pd.DataFrame, clinic: str) -> pd.DataFrame:
    """@brief Select the rows of one clinic.

    @param yearly The yearly table.
    @param clinic Name of the clinic.
    @return The rows of that clinic, in table order.
    """
    return yearly[yearly[constants.COL_CLINIC] == clinic]


def add_pct_deaths(yearly: pd.DataFrame) -> pd.DataFrame:
    """@brief Add the proportion of births that ended in a death.

    @param yearly The yearly table; it is not changed.
    @return A copy with the column pct_deaths (deaths divided by births).
    """
    result = yearly.copy()
    result[constants.COL_PCT_DEATHS] = (
        result[constants.COL_DEATHS] / result[constants.COL_BIRTHS]
    )
    return result


def average_death_rate(yearly: pd.DataFrame, clinic: str) -> float:
    """@brief Average death rate of one clinic over all years.

    @param yearly The yearly table.
    @param clinic Name of the clinic.
    @return Total deaths divided by total births, in percent.
    """
    rows = clinic_rows(yearly, clinic)
    deaths = rows[constants.COL_DEATHS].sum()
    births = rows[constants.COL_BIRTHS].sum()
    return float(deaths / births * constants.PERCENT)


def total_births_by_clinic(yearly: pd.DataFrame) -> dict[str, int]:
    """@brief Total births over all years for each clinic.

    @param yearly The yearly table.
    @return Clinic name mapped to its births.
    """
    return {
        clinic: int(clinic_rows(yearly, clinic)[constants.COL_BIRTHS].sum())
        for clinic in constants.CLINICS
    }


def busiest_clinic(yearly: pd.DataFrame) -> str:
    """@brief The clinic with the most births.

    @param yearly The yearly table.
    @return Name of that clinic.
    """
    totals = total_births_by_clinic(yearly)
    return max(totals, key=lambda clinic: totals[clinic])


def highest_deaths_by_clinic(yearly: pd.DataFrame) -> dict[str, int]:
    """@brief The highest yearly number of deaths of each clinic.

    @param yearly The yearly table.
    @return Clinic name mapped to its maximum deaths in one year.
    """
    return {
        clinic: int(clinic_rows(yearly, clinic)[constants.COL_DEATHS].max())
        for clinic in constants.CLINICS
    }


def clinic_with_higher_death_rate(yearly: pd.DataFrame) -> str:
    """@brief The clinic with the higher average death rate.

    @param yearly The yearly table.
    @return Name of that clinic.
    """
    return max(constants.CLINICS, key=lambda clinic: average_death_rate(yearly, clinic))

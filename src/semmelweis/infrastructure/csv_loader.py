"""@brief Load the CSV files shipped inside the package."""

# Python 3.13+ is required; the rule targets Python 2 compatibility.
from importlib import resources  # nosemgrep: python37-compatibility-importlib2

import pandas as pd

from semmelweis import constants


def _read_data_file(
    file_name: str, parse_dates: list[str] | None = None
) -> pd.DataFrame:
    """@brief Read one CSV file of the data package.

    @param file_name Name of the file in the data package.
    @param parse_dates Columns to parse as datetimes, if any.
    @return The file as a DataFrame.
    """
    path = resources.files(constants.DATA_PACKAGE).joinpath(file_name)
    with resources.as_file(path) as real_path:
        return pd.read_csv(real_path, parse_dates=parse_dates)


def load_yearly() -> pd.DataFrame:
    """@brief Load the yearly births and deaths of both clinics.

    @return One row per year and clinic.
    """
    return _read_data_file(constants.YEARLY_FILE)


def load_monthly() -> pd.DataFrame:
    """@brief Load the monthly births and deaths of the hospital.

    @return One row per month; the date column holds datetimes.
    """
    return _read_data_file(constants.MONTHLY_FILE, parse_dates=[constants.COL_DATE])

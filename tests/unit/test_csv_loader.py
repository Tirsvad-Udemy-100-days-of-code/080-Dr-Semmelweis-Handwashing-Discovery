"""@brief Tests for the CSV loaders."""

import pandas as pd
import pytest

from semmelweis.infrastructure import csv_loader

YEARLY_SHAPE = (12, 4)
MONTHLY_SHAPE = (98, 3)
YEARLY_COLUMNS = ["year", "births", "deaths", "clinic"]
MONTHLY_COLUMNS = ["date", "births", "deaths"]
FIRST_MONTH = pd.Timestamp("1841-01-01")
LAST_MONTH = pd.Timestamp("1849-03-01")


@pytest.fixture(name="yearly")
def fixture_yearly() -> pd.DataFrame:
    """@brief The yearly table."""
    return csv_loader.load_yearly()


@pytest.fixture(name="monthly")
def fixture_monthly() -> pd.DataFrame:
    """@brief The monthly table."""
    return csv_loader.load_monthly()


def test_load_yearly_has_expected_shape(yearly: pd.DataFrame) -> None:
    """@brief The yearly table has 12 rows and 4 columns."""
    assert yearly.shape == YEARLY_SHAPE


def test_load_yearly_has_expected_columns(yearly: pd.DataFrame) -> None:
    """@brief The yearly table has the lecture's columns."""
    assert list(yearly.columns) == YEARLY_COLUMNS


def test_load_monthly_has_expected_shape(monthly: pd.DataFrame) -> None:
    """@brief The monthly table has 98 rows and 3 columns."""
    assert monthly.shape == MONTHLY_SHAPE


def test_load_monthly_has_expected_columns(monthly: pd.DataFrame) -> None:
    """@brief The monthly table has the lecture's columns."""
    assert list(monthly.columns) == MONTHLY_COLUMNS


def test_load_monthly_parses_dates_as_datetimes(monthly: pd.DataFrame) -> None:
    """@brief The date column is a datetime column."""
    assert pd.api.types.is_datetime64_any_dtype(monthly["date"])


def test_load_monthly_starts_in_january_1841(monthly: pd.DataFrame) -> None:
    """@brief The first month is 1841-01-01."""
    assert monthly["date"].min() == FIRST_MONTH


def test_load_monthly_ends_in_march_1849(monthly: pd.DataFrame) -> None:
    """@brief The last month is 1849-03-01."""
    assert monthly["date"].max() == LAST_MONTH

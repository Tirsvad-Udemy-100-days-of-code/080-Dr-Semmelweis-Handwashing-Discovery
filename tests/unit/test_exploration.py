"""@brief Tests for the preliminary data exploration."""

import pandas as pd
import pytest

from semmelweis.domain import exploration
from semmelweis.infrastructure import csv_loader

TOLERANCE = 0.005
AVERAGE_BIRTHS = 267.0
AVERAGE_DEATHS = 22.47
PERCENT_DYING = 7.08
YEARS = [1841, 1842, 1843, 1844, 1845, 1846]


@pytest.fixture(name="yearly")
def fixture_yearly() -> pd.DataFrame:
    """@brief The yearly table."""
    return csv_loader.load_yearly()


@pytest.fixture(name="monthly")
def fixture_monthly() -> pd.DataFrame:
    """@brief The monthly table."""
    return csv_loader.load_monthly()


def test_table_shape_returns_rows_and_columns() -> None:
    """@brief The shape is (rows, columns)."""
    frame = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert exploration.table_shape(frame) == (3, 2)


def test_column_names_keeps_column_order() -> None:
    """@brief Names come back in column order."""
    frame = pd.DataFrame({"b": [1], "a": [2]})
    assert exploration.column_names(frame) == ["b", "a"]


def test_years_covered_returns_sorted_unique_years(yearly: pd.DataFrame) -> None:
    """@brief Both clinics share the years, each listed once."""
    assert exploration.years_covered(yearly) == YEARS


def test_has_nan_values_is_false_for_yearly(yearly: pd.DataFrame) -> None:
    """@brief The yearly data has no missing values."""
    assert exploration.has_nan_values(yearly) is False


def test_has_nan_values_is_false_for_monthly(monthly: pd.DataFrame) -> None:
    """@brief The monthly data has no missing values."""
    assert exploration.has_nan_values(monthly) is False


def test_has_nan_values_is_true_when_a_cell_is_missing() -> None:
    """@brief A missing cell is detected."""
    assert exploration.has_nan_values(pd.DataFrame({"a": [1.0, None]})) is True


def test_has_duplicates_is_false_for_yearly(yearly: pd.DataFrame) -> None:
    """@brief The yearly data has no duplicate rows."""
    assert exploration.has_duplicates(yearly) is False


def test_has_duplicates_is_false_for_monthly(monthly: pd.DataFrame) -> None:
    """@brief The monthly data has no duplicate rows."""
    assert exploration.has_duplicates(monthly) is False


def test_has_duplicates_is_true_when_a_row_repeats() -> None:
    """@brief A repeated row is detected."""
    assert exploration.has_duplicates(pd.DataFrame({"a": [1, 1]})) is True


def test_average_births_per_month_matches_lecture(monthly: pd.DataFrame) -> None:
    """@brief About 267 births per month."""
    result = exploration.average_births_per_month(monthly)
    assert result == pytest.approx(AVERAGE_BIRTHS, abs=TOLERANCE)


def test_average_deaths_per_month_matches_lecture(monthly: pd.DataFrame) -> None:
    """@brief About 22.47 deaths per month."""
    result = exploration.average_deaths_per_month(monthly)
    assert result == pytest.approx(AVERAGE_DEATHS, abs=TOLERANCE)


def test_percentage_of_women_dying_matches_lecture(yearly: pd.DataFrame) -> None:
    """@brief About 7.08 percent of the women died."""
    result = exploration.percentage_of_women_dying(yearly)
    assert result == pytest.approx(PERCENT_DYING, abs=TOLERANCE)


def test_percentage_of_women_dying_is_deaths_over_births() -> None:
    """@brief Ten deaths in 200 births is 5 percent."""
    frame = pd.DataFrame({"births": [100, 100], "deaths": [4, 6]})
    assert exploration.percentage_of_women_dying(frame) == pytest.approx(5.0)

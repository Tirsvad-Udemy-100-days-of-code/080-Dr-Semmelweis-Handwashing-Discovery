"""@brief Tests for the yearly data split by clinic."""

import pandas as pd
import pytest

from semmelweis.domain import clinic_split
from semmelweis.infrastructure import csv_loader

CLINIC_1 = "clinic 1"
CLINIC_2 = "clinic 2"


@pytest.fixture(name="yearly")
def fixture_yearly() -> pd.DataFrame:
    """@brief The yearly table."""
    return csv_loader.load_yearly()


def test_clinic_rows_returns_only_that_clinic(yearly: pd.DataFrame) -> None:
    """@brief Every returned row belongs to the asked clinic."""
    rows = clinic_split.clinic_rows(yearly, CLINIC_2)
    assert set(rows["clinic"]) == {CLINIC_2}


def test_clinic_rows_keeps_all_years(yearly: pd.DataFrame) -> None:
    """@brief A clinic has one row per year."""
    rows = clinic_split.clinic_rows(yearly, CLINIC_1)
    assert len(rows) == len(yearly) // 2


def test_add_pct_deaths_first_row_is_deaths_over_births(yearly: pd.DataFrame) -> None:
    """@brief 1841, clinic 1: 237 deaths in 3036 births."""
    result = clinic_split.add_pct_deaths(yearly)
    assert result["pct_deaths"].iloc[0] == pytest.approx(237 / 3036)


def test_add_pct_deaths_does_not_change_its_input(yearly: pd.DataFrame) -> None:
    """@brief The input table gets no new column."""
    clinic_split.add_pct_deaths(yearly)
    assert "pct_deaths" not in yearly.columns


def test_average_death_rate_clinic_1(yearly: pd.DataFrame) -> None:
    """@brief Clinic 1 loses about 9.92 percent."""
    assert clinic_split.average_death_rate(yearly, CLINIC_1) == pytest.approx(
        9.92, abs=0.005
    )


def test_average_death_rate_clinic_2(yearly: pd.DataFrame) -> None:
    """@brief Clinic 2 loses about 3.88 percent."""
    assert clinic_split.average_death_rate(yearly, CLINIC_2) == pytest.approx(
        3.88, abs=0.005
    )


def test_total_births_by_clinic_matches_the_data(yearly: pd.DataFrame) -> None:
    """@brief Totals equal a plain groupby sum."""
    expected = {k: int(v) for k, v in yearly.groupby("clinic")["births"].sum().items()}
    assert clinic_split.total_births_by_clinic(yearly) == expected


def test_busiest_clinic_is_clinic_1(yearly: pd.DataFrame) -> None:
    """@brief Clinic 1 has the most births."""
    assert clinic_split.busiest_clinic(yearly) == CLINIC_1


def test_highest_deaths_by_clinic_matches_the_data(yearly: pd.DataFrame) -> None:
    """@brief Maxima equal a plain groupby max."""
    expected = {k: int(v) for k, v in yearly.groupby("clinic")["deaths"].max().items()}
    assert clinic_split.highest_deaths_by_clinic(yearly) == expected


def test_highest_deaths_clinic_1_is_518(yearly: pd.DataFrame) -> None:
    """@brief Clinic 1 peaked at 518 deaths in 1842."""
    assert clinic_split.highest_deaths_by_clinic(yearly)[CLINIC_1] == 518


def test_clinic_with_higher_death_rate_is_clinic_1(yearly: pd.DataFrame) -> None:
    """@brief Clinic 1 has the higher proportion of deaths."""
    assert clinic_split.clinic_with_higher_death_rate(yearly) == CLINIC_1

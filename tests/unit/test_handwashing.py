"""@brief Tests for the effect of handwashing on the monthly data."""

import pandas as pd
import pytest

from semmelweis.domain import handwashing
from semmelweis.infrastructure import csv_loader


@pytest.fixture(name="monthly")
def fixture_monthly() -> pd.DataFrame:
    """@brief The monthly table."""
    return csv_loader.load_monthly()


def test_add_pct_deaths_monthly_first_row_is_deaths_over_births(
    monthly: pd.DataFrame,
) -> None:
    """@brief Row 0 is deaths divided by births."""
    result = handwashing.add_pct_deaths_monthly(monthly)
    expected = monthly["deaths"].iloc[0] / monthly["births"].iloc[0]
    assert result["pct_deaths"].iloc[0] == pytest.approx(expected)


def test_add_pct_deaths_monthly_does_not_change_its_input(
    monthly: pd.DataFrame,
) -> None:
    """@brief The input table gets no new column."""
    handwashing.add_pct_deaths_monthly(monthly)
    assert "pct_deaths" not in monthly.columns


def test_split_before_after_sizes(monthly: pd.DataFrame) -> None:
    """@brief 76 months before June 1847 and 22 from then on."""
    before, after = handwashing.split_before_after(monthly)
    assert (len(before), len(after)) == (76, 22)


def test_split_before_after_covers_all_rows_without_overlap(
    monthly: pd.DataFrame,
) -> None:
    """@brief Every month lands in exactly one period."""
    before, after = handwashing.split_before_after(monthly)
    assert len(before) + len(after) == len(monthly)
    assert before["date"].max() < pd.Timestamp("1847-06-01") <= after["date"].min()


def test_split_before_after_accepts_another_start(monthly: pd.DataFrame) -> None:
    """@brief A later start moves months to the first period."""
    before, _ = handwashing.split_before_after(monthly, "1847-07-01")
    assert len(before) == 77


def test_average_rate_before_after_matches_the_lecture(
    monthly: pd.DataFrame,
) -> None:
    """@brief About 10.53 percent before and 2.15 percent after."""
    before, after = handwashing.average_rate_before_after(monthly)
    assert before == pytest.approx(10.53, abs=0.01)
    assert after == pytest.approx(2.15, abs=0.01)


def test_mean_of_rates_before_after_matches_the_lecture(
    monthly: pd.DataFrame,
) -> None:
    """@brief About 10.50 percent before and 2.11 percent after."""
    before, after = handwashing.mean_of_rates_before_after(monthly)
    assert before == pytest.approx(10.50, abs=0.01)
    assert after == pytest.approx(2.11, abs=0.01)


def test_improvement_factor_is_before_over_after() -> None:
    """@brief 10 percent down to 2 percent is a factor 5."""
    assert handwashing.improvement_factor(10.0, 2.0) == pytest.approx(5.0)


def test_improvement_factor_for_the_data_is_about_five(
    monthly: pd.DataFrame,
) -> None:
    """@brief Handwashing cut the death rate about five times."""
    factor = handwashing.improvement_factor(
        *handwashing.average_rate_before_after(monthly)
    )
    assert factor == pytest.approx(4.89, abs=0.01)


def test_rolling_average_starts_after_a_full_window(monthly: pd.DataFrame) -> None:
    """@brief The first five months have no average, the sixth has."""
    result = handwashing.rolling_average(monthly, window=6)
    column = result["rolling_pct_deaths"]
    assert column.iloc[:5].isna().all()
    expected = (monthly["deaths"] / monthly["births"]).iloc[:6].mean()
    assert column.iloc[5] == pytest.approx(expected)


def test_rolling_average_does_not_change_its_input(monthly: pd.DataFrame) -> None:
    """@brief The input table is left as it was."""
    handwashing.rolling_average(monthly)
    assert list(monthly.columns) == ["date", "births", "deaths"]


def test_rolling_average_default_window_is_six_months(
    monthly: pd.DataFrame,
) -> None:
    """@brief The default window equals an explicit window of six."""
    default = handwashing.rolling_average(monthly)["rolling_pct_deaths"]
    explicit = handwashing.rolling_average(monthly, window=6)["rolling_pct_deaths"]
    pd.testing.assert_series_equal(default, explicit)

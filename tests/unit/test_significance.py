"""@brief Tests for the significance test of the handwashing effect."""

import numpy as np
import pandas as pd
import pytest

from semmelweis.domain import handwashing, significance
from semmelweis.infrastructure import csv_loader


@pytest.fixture(name="marked")
def fixture_marked() -> pd.DataFrame:
    """@brief The monthly table with pct_deaths and washing_hands."""
    monthly = handwashing.add_pct_deaths_monthly(csv_loader.load_monthly())
    return significance.add_washing_hands(monthly)


def test_add_washing_hands_counts_76_without_and_22_with(
    marked: pd.DataFrame,
) -> None:
    """@brief 76 months before June 1847 and 22 from then on."""
    counts = marked["washing_hands"].value_counts()
    assert (counts[False], counts[True]) == (76, 22)


def test_add_washing_hands_flags_the_start_month_as_washing() -> None:
    """@brief The start day itself belongs to the handwashing period."""
    frame = pd.DataFrame({"date": pd.to_datetime(["1847-05-01", "1847-06-01"])})
    result = significance.add_washing_hands(frame)
    assert result["washing_hands"].tolist() == [False, True]


def test_add_washing_hands_does_not_change_its_input() -> None:
    """@brief The input table gets no new column."""
    frame = pd.DataFrame({"date": pd.to_datetime(["1847-05-01"])})
    significance.add_washing_hands(frame)
    assert list(frame.columns) == ["date"]


def test_group_means_match_the_lecture(marked: pd.DataFrame) -> None:
    """@brief About 10.5 percent without and 2.11 percent with handwashing."""
    without, with_washing = significance.group_means(marked)
    assert without == pytest.approx(0.105, abs=0.0001)
    assert with_washing == pytest.approx(0.0211, abs=0.0001)


def test_two_sample_t_test_matches_the_lecture(marked: pd.DataFrame) -> None:
    """@brief t is about 5.51 and p about 3e-7."""
    rates = marked["pct_deaths"]
    washing = marked["washing_hands"]
    result = significance.two_sample_t_test(rates[~washing], rates[washing])
    assert result.statistic == pytest.approx(5.512, abs=0.001)
    assert result.p_value == pytest.approx(2.985e-7, rel=0.01)


def test_two_sample_t_test_of_equal_samples_is_not_significant() -> None:
    """@brief Identical samples give t of zero and p of one."""
    sample = pd.Series([1.0, 2.0, 3.0, 4.0])
    result = significance.two_sample_t_test(sample, sample)
    assert result.statistic == pytest.approx(0.0)
    assert result.p_value == pytest.approx(1.0)


def test_is_significant_for_the_lecture_p_value() -> None:
    """@brief 2.985e-7 is below the 99 percent level."""
    assert significance.is_significant(2.985e-7)


def test_is_significant_is_false_at_the_limit() -> None:
    """@brief p equal to alpha is not below it."""
    assert not significance.is_significant(0.01)


def test_is_significant_accepts_another_alpha() -> None:
    """@brief 0.03 passes at the 95 percent level only."""
    assert significance.is_significant(0.03, alpha=0.05)
    assert not significance.is_significant(0.03)


def test_kde_curve_stays_inside_the_data_range(marked: pd.DataFrame) -> None:
    """@brief The grid runs from the sample minimum to its maximum."""
    rates = marked["pct_deaths"]
    grid, density = significance.kde_curve(rates)
    assert grid[0] == pytest.approx(rates.min())
    assert grid[-1] == pytest.approx(rates.max())
    assert len(grid) == len(density) == 200
    assert np.all(density > 0)

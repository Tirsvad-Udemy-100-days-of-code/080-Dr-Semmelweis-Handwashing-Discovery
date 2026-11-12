"""@brief Tests for the handwashing chart."""

from collections.abc import Iterator

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import pytest
from matplotlib.axes import Axes

from semmelweis.infrastructure import csv_loader
from semmelweis.presentation import charts


@pytest.fixture(name="monthly")
def fixture_monthly() -> pd.DataFrame:
    """@brief The monthly table."""
    return csv_loader.load_monthly()


@pytest.fixture(name="ax")
def fixture_ax(monthly: pd.DataFrame) -> Iterator[Axes]:
    """@brief Axis of the handwashing chart."""
    fig = charts.handwashing_chart(monthly)
    yield fig.axes[0]
    plt.close(fig)


def test_chart_has_one_axis(ax: Axes) -> None:
    """@brief A single time series axis."""
    assert len(ax.figure.axes) == 1


def test_chart_has_title_and_axis_labels(ax: Axes) -> None:
    """@brief Title and both axes are labelled."""
    assert "handwashing" in ax.get_title().lower()
    assert ax.get_xlabel() == "Month"
    assert ax.get_ylabel() == "Percentage of Monthly Deaths"


def test_chart_draws_both_periods_and_the_rolling_average(ax: Axes) -> None:
    """@brief Before, after, rolling average and the start marker are drawn."""
    labels = [line.get_label() for line in ax.lines]
    assert labels == [
        "Before handwashing",
        "After handwashing",
        "6-month rolling average",
        "Handwashing made mandatory",
    ]


def test_chart_periods_have_the_split_sizes(ax: Axes) -> None:
    """@brief The period lines hold 76 and 22 months."""
    assert (len(ax.lines[0].get_xdata()), len(ax.lines[1].get_xdata())) == (76, 22)


def test_chart_periods_have_different_colours(ax: Axes) -> None:
    """@brief Before and after can be told apart."""
    assert ax.lines[0].get_color() != ax.lines[1].get_color()


def test_chart_marks_the_start_date(ax: Axes) -> None:
    """@brief The vertical marker sits on the handwashing start."""
    x = mdates.date2num(ax.lines[3].get_xdata()[0])
    assert x == pytest.approx(float(mdates.date2num(pd.Timestamp("1847-06-01"))))


def test_chart_legend_names_every_line(ax: Axes) -> None:
    """@brief The legend has an entry for each drawn line."""
    legend = ax.get_legend()
    assert legend is not None
    assert [t.get_text() for t in legend.get_texts()] == [
        line.get_label() for line in ax.lines
    ]


def test_chart_does_not_change_its_input(monthly: pd.DataFrame) -> None:
    """@brief The input table gets no new column."""
    fig = charts.handwashing_chart(monthly)
    plt.close(fig)
    assert list(monthly.columns) == ["date", "births", "deaths"]

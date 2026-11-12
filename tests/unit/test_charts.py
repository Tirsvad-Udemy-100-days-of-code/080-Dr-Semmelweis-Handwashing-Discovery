"""@brief Tests for the lecture charts."""

from collections.abc import Iterator

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import pytest
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from semmelweis.infrastructure import csv_loader
from semmelweis.presentation import charts

TITLE = "Total Number of Monthly Births and Deaths"


@pytest.fixture(name="monthly")
def fixture_monthly() -> pd.DataFrame:
    """@brief The monthly table."""
    return csv_loader.load_monthly()


@pytest.fixture(name="figure")
def fixture_figure(monthly: pd.DataFrame) -> Iterator[Figure]:
    """@brief The chart, closed after the test."""
    fig = charts.births_and_deaths_chart(monthly)
    yield fig
    plt.close(fig)


@pytest.fixture(name="births_ax")
def fixture_births_ax(figure: Figure) -> Axes:
    """@brief The axis holding the births line."""
    return figure.axes[0]


@pytest.fixture(name="deaths_ax")
def fixture_deaths_ax(figure: Figure) -> Axes:
    """@brief The twin axis holding the deaths line."""
    return figure.axes[1]


def test_chart_has_two_axes(figure: Figure) -> None:
    """@brief Births and deaths have their own y-axis."""
    assert len(figure.axes) == 2


def test_chart_title_is_set(births_ax: Axes) -> None:
    """@brief The title names the chart."""
    assert births_ax.get_title() == TITLE


def test_births_line_is_skyblue(births_ax: Axes) -> None:
    """@brief Births are drawn in skyblue."""
    assert births_ax.lines[0].get_color() == "skyblue"


def test_births_line_width_is_three(births_ax: Axes) -> None:
    """@brief Births are drawn with width 3."""
    assert births_ax.lines[0].get_linewidth() == 3


def test_deaths_line_is_crimson(deaths_ax: Axes) -> None:
    """@brief Deaths are drawn in crimson."""
    assert deaths_ax.lines[0].get_color() == "crimson"


def test_deaths_line_width_is_two(deaths_ax: Axes) -> None:
    """@brief Deaths are drawn with width 2."""
    assert deaths_ax.lines[0].get_linewidth() == 2


def test_deaths_line_is_dashed(deaths_ax: Axes) -> None:
    """@brief Deaths are drawn dashed."""
    assert deaths_ax.lines[0].get_linestyle() == "--"


def test_births_label_is_skyblue(births_ax: Axes) -> None:
    """@brief The left y label says Births in the line colour."""
    label = births_ax.yaxis.label
    assert (label.get_text(), label.get_color()) == ("Births", "skyblue")


def test_deaths_label_is_crimson(deaths_ax: Axes) -> None:
    """@brief The right y label says Deaths in the line colour."""
    label = deaths_ax.yaxis.label
    assert (label.get_text(), label.get_color()) == ("Deaths", "crimson")


def test_xlim_starts_at_first_date(births_ax: Axes, monthly: pd.DataFrame) -> None:
    """@brief The lines touch the left axis."""
    first = mdates.date2num(monthly["date"].iloc[0])
    assert births_ax.get_xlim()[0] == pytest.approx(first)


def test_xlim_ends_at_last_date(births_ax: Axes, monthly: pd.DataFrame) -> None:
    """@brief The lines touch the right axis."""
    last = mdates.date2num(monthly["date"].iloc[-1])
    assert births_ax.get_xlim()[1] == pytest.approx(last)


def test_x_axis_has_year_major_ticks(births_ax: Axes) -> None:
    """@brief Major ticks are years."""
    assert isinstance(births_ax.xaxis.get_major_locator(), mdates.YearLocator)


def test_x_axis_has_month_minor_ticks(births_ax: Axes) -> None:
    """@brief Minor ticks are months."""
    assert isinstance(births_ax.xaxis.get_minor_locator(), mdates.MonthLocator)


def test_x_axis_formats_ticks_as_year(births_ax: Axes) -> None:
    """@brief Major tick labels show the year only."""
    formatter = births_ax.xaxis.get_major_formatter()
    assert isinstance(formatter, mdates.DateFormatter)
    assert formatter.fmt == "%Y"

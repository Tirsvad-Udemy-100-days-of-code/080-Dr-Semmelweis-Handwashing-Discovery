"""@brief Tests for the charts of the yearly data split by clinic."""

from collections.abc import Callable, Iterator

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from semmelweis.infrastructure import csv_loader
from semmelweis.presentation import charts

CLINIC_LABELS = ["clinic 1", "clinic 2"]


@pytest.fixture(name="yearly")
def fixture_yearly() -> pd.DataFrame:
    """@brief The yearly table."""
    return csv_loader.load_yearly()


def _first_axis(make: Callable[[pd.DataFrame], Figure], yearly: pd.DataFrame) -> Axes:
    """@brief Draw a chart and return its axis; the figure is closed after."""
    fig = make(yearly)
    plt.close(fig)
    return fig.axes[0]


@pytest.fixture(name="births_ax")
def fixture_births_ax(yearly: pd.DataFrame) -> Iterator[Axes]:
    """@brief Axis of the births chart."""
    yield _first_axis(charts.births_by_clinic_chart, yearly)


@pytest.mark.parametrize(
    ("make", "title"),
    [
        (charts.births_by_clinic_chart, "Total Yearly Births by Clinic"),
        (charts.deaths_by_clinic_chart, "Total Yearly Deaths by Clinic"),
        (charts.pct_deaths_by_clinic_chart, "Proportion of Yearly Deaths by Clinic"),
    ],
)
def test_wrapper_chart_has_title_and_one_line_per_clinic(
    make: Callable[[pd.DataFrame], Figure], title: str, yearly: pd.DataFrame
) -> None:
    """@brief Each wrapper has its lecture title and a labelled line per clinic."""
    ax = _first_axis(make, yearly)
    assert ax.get_title() == title
    assert [line.get_label() for line in ax.lines] == CLINIC_LABELS


def test_legend_shows_the_clinic_names(births_ax: Axes) -> None:
    """@brief The legend names both clinics."""
    legend = births_ax.get_legend()
    assert legend is not None
    assert [t.get_text() for t in legend.get_texts()] == CLINIC_LABELS


def test_clinic_lines_have_different_colours(births_ax: Axes) -> None:
    """@brief The two clinics can be told apart."""
    colours = {line.get_color() for line in births_ax.lines}
    assert len(colours) == 2


def test_x_axis_is_year_with_integer_ticks(births_ax: Axes) -> None:
    """@brief Ticks are whole years, labelled Year."""
    fig = births_ax.figure
    fig.canvas.draw()
    ticks = births_ax.get_xticks()
    assert births_ax.get_xlabel() == "Year"
    assert all(float(t).is_integer() for t in ticks)


def test_yearly_line_chart_draws_the_given_column(yearly: pd.DataFrame) -> None:
    """@brief The y data of clinic 1 is the deaths column."""
    fig = charts.yearly_line_chart(yearly, "deaths", "Any title")
    plt.close(fig)
    first = fig.axes[0].lines[0].get_ydata()
    expected = yearly[yearly["clinic"] == "clinic 1"]["deaths"].to_numpy()
    assert list(first) == list(expected)


def test_pct_deaths_chart_adds_the_column_itself(yearly: pd.DataFrame) -> None:
    """@brief The input table is left without pct_deaths."""
    fig = charts.pct_deaths_by_clinic_chart(yearly)
    plt.close(fig)
    assert "pct_deaths" not in yearly.columns


def test_overview_chart_has_three_axes(yearly: pd.DataFrame) -> None:
    """@brief Births, deaths and proportion each get an axis."""
    fig = charts.clinic_overview_chart(yearly)
    plt.close(fig)
    assert len(fig.axes) == 3

"""@brief Tests for the distribution charts of lecture 595."""

from collections.abc import Iterator

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from matplotlib.axes import Axes

from semmelweis.domain import handwashing
from semmelweis.infrastructure import csv_loader
from semmelweis.presentation import charts


@pytest.fixture(name="monthly")
def fixture_monthly() -> pd.DataFrame:
    """@brief The monthly table."""
    return csv_loader.load_monthly()


def _legend_texts(ax: Axes) -> list[str]:
    """@brief Texts of the legend of an axis."""
    legend = ax.get_legend()
    assert legend is not None
    return [t.get_text() for t in legend.get_texts()]


@pytest.fixture(name="box_ax")
def fixture_box_ax(monthly: pd.DataFrame) -> Iterator[Axes]:
    """@brief Axis of the box plot."""
    fig = charts.box_plot_chart(monthly)
    yield fig.axes[0]
    plt.close(fig)


@pytest.fixture(name="hist_ax")
def fixture_hist_ax(monthly: pd.DataFrame) -> Iterator[Axes]:
    """@brief Axis of the histogram chart."""
    fig = charts.histogram_overlay_chart(monthly)
    yield fig.axes[0]
    plt.close(fig)


@pytest.fixture(name="kde_ax")
def fixture_kde_ax(monthly: pd.DataFrame) -> Iterator[Axes]:
    """@brief Axis of the KDE chart."""
    fig = charts.kde_chart(monthly)
    yield fig.axes[0]
    plt.close(fig)


def test_box_plot_has_two_boxes_with_labels(box_ax: Axes) -> None:
    """@brief One box per group, labelled No and Yes."""
    assert [t.get_text() for t in box_ax.get_xticklabels()] == ["No", "Yes"]
    assert len(box_ax.lines) > 0


def test_box_plot_has_title_and_axis_labels(box_ax: Axes) -> None:
    """@brief Title and both axes are labelled."""
    assert "handwashing" in box_ax.get_title().lower()
    assert box_ax.get_xlabel() == "Washing Hands?"
    assert box_ax.get_ylabel() == "Percentage of Monthly Deaths"


def test_box_plot_medians_differ_by_group(box_ax: Axes) -> None:
    """@brief The median without handwashing is above the one with it."""
    medians = [line.get_ydata()[0] for line in box_ax.lines[4::7]]
    assert len(medians) == 2
    assert medians[0] > medians[1]


def test_histogram_draws_both_groups_with_30_bins_each(hist_ax: Axes) -> None:
    """@brief Two bar containers of 30 bars."""
    assert [len(c) for c in hist_ax.containers] == [30, 30]


def test_histogram_is_normalised_to_percent(hist_ax: Axes) -> None:
    """@brief Each group's bar heights add up to 100 percent."""
    for container in hist_ax.containers:
        total = sum(bar.get_height() for bar in container)
        assert total == pytest.approx(100.0)


def test_histogram_bars_are_translucent(hist_ax: Axes) -> None:
    """@brief The bars use alpha 0.6 so both groups stay visible."""
    assert hist_ax.patches[0].get_alpha() == pytest.approx(0.6)


def test_histogram_has_legend_and_labels(hist_ax: Axes) -> None:
    """@brief Legend names both groups; axes are labelled."""
    assert _legend_texts(hist_ax) == ["Without handwashing", "With handwashing"]
    assert hist_ax.get_xlabel() == "Percentage of Monthly Deaths"
    assert hist_ax.get_ylabel() == "Percent of months"
    assert hist_ax.get_title() != ""


def test_kde_has_one_curve_per_group_and_legend(kde_ax: Axes) -> None:
    """@brief Two lines, named in the legend."""
    assert len(kde_ax.lines) == 2
    assert _legend_texts(kde_ax) == ["Without handwashing", "With handwashing"]


def test_kde_is_clipped_to_the_data_range(kde_ax: Axes, monthly: pd.DataFrame) -> None:
    """@brief Each curve starts at its minimum and ends at its maximum."""
    data = handwashing.add_pct_deaths_monthly(monthly)
    before, after = handwashing.split_before_after(data)
    for line, group in zip(kde_ax.lines, (before, after), strict=True):
        x = np.asarray(line.get_xdata(), dtype=float)
        assert x.min() == pytest.approx(group["pct_deaths"].min())
        assert x.max() == pytest.approx(group["pct_deaths"].max())


def test_kde_has_labels(kde_ax: Axes) -> None:
    """@brief Title and axes are labelled."""
    assert "density" in kde_ax.get_title().lower()
    assert kde_ax.get_xlabel() == "Percentage of Monthly Deaths"
    assert kde_ax.get_ylabel() == "Probability density"


def test_overview_has_three_axes(monthly: pd.DataFrame) -> None:
    """@brief Box plot, histogram and KDE side by side."""
    fig = charts.distributions_overview_chart(monthly)
    plt.close(fig)
    assert len(fig.axes) == 3


def test_charts_do_not_change_their_input(monthly: pd.DataFrame) -> None:
    """@brief The input table gets no new column."""
    for draw in (
        charts.box_plot_chart,
        charts.histogram_overlay_chart,
        charts.kde_chart,
    ):
        plt.close(draw(monthly))
    assert list(monthly.columns) == ["date", "births", "deaths"]

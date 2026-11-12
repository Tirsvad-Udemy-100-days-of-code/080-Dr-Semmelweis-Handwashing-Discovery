"""@brief Charts drawn for the lectures."""

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from semmelweis import constants


def _style_value_axis(ax: Axes, label: str, color: str) -> None:
    """@brief Label a y-axis and colour the label like its line.

    @param ax The axis.
    @param label Text of the y label.
    @param color Colour of the label.
    """
    ax.set_ylabel(label, color=color, fontsize=constants.AXIS_LABEL_FONT_SIZE)
    ax.tick_params(
        axis="y",
        labelsize=constants.TICK_FONT_SIZE,
        labelrotation=constants.TICK_ROTATION,
    )


def births_and_deaths_chart(monthly: pd.DataFrame) -> Figure:
    """@brief Draw monthly births and deaths on two y-axes (lecture 592).

    @param monthly The monthly table.
    @return The figure; the caller shows or saves it.
    """
    dates = monthly[constants.COL_DATE]
    fig, births_ax = plt.subplots(
        figsize=constants.FIGURE_SIZE, dpi=constants.FIGURE_DPI
    )
    deaths_ax = births_ax.twinx()
    births_ax.set_title(constants.CHART_TITLE, fontsize=constants.CHART_TITLE_FONT_SIZE)
    births_ax.xaxis.set_major_locator(mdates.YearLocator())
    births_ax.xaxis.set_major_formatter(mdates.DateFormatter(constants.YEAR_FORMAT))
    births_ax.xaxis.set_minor_locator(mdates.MonthLocator())
    births_ax.set_xlim(dates.min(), dates.max())
    births_ax.grid(color=constants.GRID_COLOR, linestyle=constants.GRID_LINESTYLE)
    births_ax.plot(
        dates,
        monthly[constants.COL_BIRTHS],
        color=constants.COLOR_BIRTHS,
        linewidth=constants.LINEWIDTH_BIRTHS,
    )
    deaths_ax.plot(
        dates,
        monthly[constants.COL_DEATHS],
        color=constants.COLOR_DEATHS,
        linewidth=constants.LINEWIDTH_DEATHS,
        linestyle=constants.LINESTYLE_DEATHS,
    )
    _style_value_axis(births_ax, constants.LABEL_BIRTHS, constants.COLOR_BIRTHS)
    _style_value_axis(deaths_ax, constants.LABEL_DEATHS, constants.COLOR_DEATHS)
    births_ax.tick_params(
        axis="x",
        labelsize=constants.TICK_FONT_SIZE,
        labelrotation=constants.TICK_ROTATION,
    )
    fig.tight_layout()
    return fig

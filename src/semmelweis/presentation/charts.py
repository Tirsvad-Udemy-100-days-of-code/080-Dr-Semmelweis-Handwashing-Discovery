"""@brief Charts drawn for the lectures."""

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator, PercentFormatter

from semmelweis import constants
from semmelweis.domain.clinic_split import add_pct_deaths, clinic_rows
from semmelweis.domain.handwashing import rolling_average, split_before_after


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


def _draw_clinic_lines(ax: Axes, yearly: pd.DataFrame, column: str, title: str) -> None:
    """@brief Draw one line per clinic on an axis.

    @param ax The axis.
    @param yearly The yearly table.
    @param column Column drawn on the y-axis.
    @param title Title of the axis.
    """
    for clinic in constants.CLINICS:
        rows = clinic_rows(yearly, clinic)
        ax.plot(
            rows[constants.COL_YEAR],
            rows[column],
            color=constants.CLINIC_COLORS[clinic],
            linewidth=constants.CLINIC_LINEWIDTH,
            label=clinic,
        )
    ax.set_title(title, fontsize=constants.CHART_TITLE_FONT_SIZE)
    ax.set_xlabel(constants.LABEL_YEAR, fontsize=constants.AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(column, fontsize=constants.AXIS_LABEL_FONT_SIZE)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(color=constants.GRID_COLOR, linestyle=constants.GRID_LINESTYLE)
    ax.legend(fontsize=constants.CLINIC_LEGEND_FONT_SIZE)


def yearly_line_chart(yearly: pd.DataFrame, column: str, title: str) -> Figure:
    """@brief Draw one yearly column as a line per clinic (lecture 593).

    @param yearly The yearly table.
    @param column Column drawn on the y-axis.
    @param title Title of the chart.
    @return The figure; the caller shows or saves it.
    """
    fig, ax = plt.subplots(figsize=constants.FIGURE_SIZE, dpi=constants.FIGURE_DPI)
    _draw_clinic_lines(ax, yearly, column, title)
    fig.tight_layout()
    return fig


def births_by_clinic_chart(yearly: pd.DataFrame) -> Figure:
    """@brief Draw the yearly births of each clinic.

    @param yearly The yearly table.
    @return The figure.
    """
    return yearly_line_chart(
        yearly, constants.COL_BIRTHS, constants.TITLE_BIRTHS_BY_CLINIC
    )


def deaths_by_clinic_chart(yearly: pd.DataFrame) -> Figure:
    """@brief Draw the yearly deaths of each clinic.

    @param yearly The yearly table.
    @return The figure.
    """
    return yearly_line_chart(
        yearly, constants.COL_DEATHS, constants.TITLE_DEATHS_BY_CLINIC
    )


def _with_pct_deaths(yearly: pd.DataFrame) -> pd.DataFrame:
    """@brief Return the table with the pct_deaths column present.

    @param yearly The yearly table.
    @return The same table when it has the column, else a copy that has it.
    """
    if constants.COL_PCT_DEATHS in yearly.columns:
        return yearly
    return add_pct_deaths(yearly)


def pct_deaths_by_clinic_chart(yearly: pd.DataFrame) -> Figure:
    """@brief Draw the yearly proportion of deaths of each clinic.

    @param yearly The yearly table; pct_deaths is added when missing.
    @return The figure.
    """
    return yearly_line_chart(
        _with_pct_deaths(yearly),
        constants.COL_PCT_DEATHS,
        constants.TITLE_PCT_DEATHS_BY_CLINIC,
    )


def clinic_overview_chart(yearly: pd.DataFrame) -> Figure:
    """@brief Draw births, deaths and proportion of deaths side by side.

    @param yearly The yearly table; pct_deaths is added when missing.
    @return A figure with three axes.
    """
    data = _with_pct_deaths(yearly)
    fig, axes = plt.subplots(
        1,
        3,
        figsize=constants.CLINIC_OVERVIEW_FIGURE_SIZE,
        dpi=constants.FIGURE_DPI,
    )
    panels = (
        (constants.COL_BIRTHS, constants.TITLE_BIRTHS_BY_CLINIC),
        (constants.COL_DEATHS, constants.TITLE_DEATHS_BY_CLINIC),
        (constants.COL_PCT_DEATHS, constants.TITLE_PCT_DEATHS_BY_CLINIC),
    )
    for ax, (column, title) in zip(axes, panels, strict=True):
        _draw_clinic_lines(ax, data, column, title)
        ax.title.set_fontsize(constants.CLINIC_OVERVIEW_TITLE_FONT_SIZE)
    fig.tight_layout()
    return fig


def _draw_period(ax: Axes, rows: pd.DataFrame, color: str, label: str) -> None:
    """@brief Draw the monthly proportion of deaths of one period.

    @param ax The axis.
    @param rows Rows of the period, with the column pct_deaths.
    @param color Colour of the line.
    @param label Legend entry of the line.
    """
    ax.plot(
        rows[constants.COL_DATE],
        rows[constants.COL_PCT_DEATHS],
        color=color,
        linewidth=constants.LINEWIDTH_PCT_DEATHS,
        label=label,
    )


def handwashing_chart(monthly: pd.DataFrame) -> Figure:
    """@brief Draw the monthly proportion of deaths around handwashing (lecture 594).

    @param monthly The monthly table; pct_deaths is added when missing.
    @return The figure; the caller shows or saves it.
    """
    data = rolling_average(monthly)
    before, after = split_before_after(data)
    start = pd.Timestamp(constants.HANDWASHING_START)
    fig, ax = plt.subplots(figsize=constants.FIGURE_SIZE, dpi=constants.FIGURE_DPI)
    _draw_period(
        ax,
        before,
        constants.COLOR_BEFORE_HANDWASHING,
        constants.LABEL_BEFORE_HANDWASHING,
    )
    _draw_period(
        ax, after, constants.COLOR_AFTER_HANDWASHING, constants.LABEL_AFTER_HANDWASHING
    )
    ax.plot(
        data[constants.COL_DATE],
        data[constants.COL_ROLLING_PCT_DEATHS],
        color=constants.COLOR_ROLLING_AVERAGE,
        linewidth=constants.LINEWIDTH_ROLLING_AVERAGE,
        linestyle=constants.LINESTYLE_ROLLING_AVERAGE,
        label=constants.LABEL_ROLLING_AVERAGE,
    )
    ax.axvline(
        start,
        color=constants.COLOR_HANDWASHING_START,
        linestyle=constants.LINESTYLE_HANDWASHING_START,
        label=constants.LABEL_HANDWASHING_START,
    )
    ax.set_title(constants.TITLE_HANDWASHING, fontsize=constants.CHART_TITLE_FONT_SIZE)
    ax.set_xlabel(constants.LABEL_MONTH, fontsize=constants.AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(constants.LABEL_PCT_DEATHS, fontsize=constants.AXIS_LABEL_FONT_SIZE)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter(constants.YEAR_FORMAT))
    ax.tick_params(labelsize=constants.TICK_FONT_SIZE)
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
    ax.grid(color=constants.GRID_COLOR, linestyle=constants.GRID_LINESTYLE)
    ax.legend(fontsize=constants.HANDWASHING_LEGEND_FONT_SIZE)
    fig.tight_layout()
    return fig

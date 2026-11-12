"""@brief Generate one picture per lecture step for the README and the wiki.

@details Run from the repository root::

    python -m semmelweis.presentation.screenshots

Each picture is drawn by the code of its step, so it always matches the code.
"""

from __future__ import annotations

import argparse
import logging
from collections.abc import Callable
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402
from matplotlib.ticker import PercentFormatter  # noqa: E402

from semmelweis import constants  # noqa: E402
from semmelweis.domain.handwashing import (  # noqa: E402
    add_pct_deaths_monthly,
    average_rate_before_after,
    improvement_factor,
    rolling_average,
    split_before_after,
)
from semmelweis.domain.significance import (  # noqa: E402
    is_significant,
    two_sample_t_test,
)
from semmelweis.infrastructure.csv_loader import (  # noqa: E402
    load_monthly,
    load_yearly,
)
from semmelweis.presentation.charts import (  # noqa: E402
    births_and_deaths_chart,
    clinic_overview_chart,
    distributions_overview_chart,
    handwashing_chart,
)

_LOG = logging.getLogger(__name__)
DEFAULT_OUTPUT_DIR = Path(*constants.IMAGES_DIR)


def _draw_table(ax: Axes, frame: pd.DataFrame, title: str) -> None:
    """@brief Draw the first rows of a DataFrame as a table on an axis.

    @param ax Axis to draw on.
    @param frame Data to show; only the first rows are drawn.
    @param title Heading above the table.
    """
    ax.axis("off")
    ax.set_title(
        title, fontsize=constants.TABLE_TITLE_FONT_SIZE, pad=constants.TABLE_TITLE_PAD
    )
    preview = frame.head(constants.PREVIEW_ROWS)
    table = ax.table(
        cellText=preview.astype(str).to_numpy(),
        colLabels=list(preview.columns),
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(constants.TABLE_FONT_SIZE)
    table.scale(1, constants.TABLE_ROW_SCALE)


def step_1_goals() -> Figure:
    """@brief Draw the data the project works with (lecture 591).

    @return A figure with the first rows of the yearly and the monthly table.
    """
    yearly = load_yearly()
    monthly = load_monthly()
    fig, (left, right) = plt.subplots(
        1,
        2,
        figsize=constants.OVERVIEW_FIGURE_SIZE,
        dpi=constants.FIGURE_DPI,
    )
    fig.suptitle(
        constants.OVERVIEW_TITLE,
        fontsize=constants.SUPTITLE_FONT_SIZE,
        fontweight="bold",
    )
    _draw_table(left, yearly, f"{constants.YEARLY_FILE}  ({len(yearly)} rows)")
    _draw_table(right, monthly, f"{constants.MONTHLY_FILE}  ({len(monthly)} rows)")
    fig.tight_layout()
    return fig


def step_2_data_exploration() -> Figure:
    """@brief Draw monthly births and deaths (lecture 592).

    @return The twin-axis line chart.
    """
    return births_and_deaths_chart(load_monthly())


def step_3_clinic_split() -> Figure:
    """@brief Draw the yearly data split by clinic (lecture 593).

    @return A figure with births, deaths and proportion of deaths per clinic.
    """
    return clinic_overview_chart(load_yearly())


def step_4_handwashing_effect() -> Figure:
    """@brief Draw the monthly proportion of deaths around handwashing (lecture 594).

    @return The time series with the rolling average and the handwashing start.
    """
    return handwashing_chart(load_monthly())


def step_5_distributions() -> Figure:
    """@brief Draw the distributions of the monthly death rate (lecture 595).

    @return A figure with the box plot, the histograms and the KDE.
    """
    return distributions_overview_chart(load_monthly())


def summary_lines(monthly: pd.DataFrame) -> list[str]:
    """@brief Compute the headline results of the study as text lines.

    @param monthly The monthly table.
    @return One line each for the rates, the factor, t, p and the verdict.
    """
    before_rate, after_rate = average_rate_before_after(monthly)
    data = add_pct_deaths_monthly(monthly)
    before, after = split_before_after(data)
    result = two_sample_t_test(
        before[constants.COL_PCT_DEATHS], after[constants.COL_PCT_DEATHS]
    )
    verdict = (
        constants.LABEL_YES if is_significant(result.p_value) else constants.LABEL_NO
    )
    return [
        constants.SUMMARY_LINE_BEFORE.format(before_rate),
        constants.SUMMARY_LINE_AFTER.format(after_rate),
        constants.SUMMARY_LINE_FACTOR.format(
            improvement_factor(before_rate, after_rate)
        ),
        constants.SUMMARY_LINE_T_STATISTIC.format(result.statistic),
        constants.SUMMARY_LINE_P_VALUE.format(result.p_value),
        constants.SUMMARY_LINE_SIGNIFICANT.format(
            constants.SIGNIFICANCE_LEVEL, verdict
        ),
    ]


def _draw_summary_panel(ax: Axes, lines: list[str]) -> None:
    """@brief Draw the heading and the result lines on a blank axis.

    @param ax Axis to draw on.
    @param lines The result lines, top to bottom.
    """
    ax.axis("off")
    ax.add_patch(
        Rectangle(
            (0, 0),
            1,
            1,
            transform=ax.transAxes,
            facecolor=constants.SUMMARY_BOX_COLOR,
            edgecolor=constants.GRID_COLOR,
        )
    )
    ax.text(
        constants.SUMMARY_TEXT_X,
        constants.SUMMARY_HEADING_Y,
        constants.SUMMARY_HEADING,
        transform=ax.transAxes,
        fontsize=constants.SUMMARY_HEADING_FONT_SIZE,
        fontweight="bold",
        va="top",
    )
    ax.text(
        constants.SUMMARY_TEXT_X,
        constants.SUMMARY_TEXT_Y,
        "\n".join(lines),
        transform=ax.transAxes,
        fontsize=constants.SUMMARY_TEXT_FONT_SIZE,
        linespacing=constants.SUMMARY_LINE_SPACING,
        va="top",
    )


def _draw_summary_series(ax: Axes, monthly: pd.DataFrame) -> None:
    """@brief Draw the monthly death rate with its rolling average.

    @param ax Axis to draw on.
    @param monthly The monthly table.
    """
    data = rolling_average(monthly)
    ax.plot(
        data[constants.COL_DATE],
        data[constants.COL_PCT_DEATHS],
        color=constants.COLOR_DEATHS,
        linewidth=constants.LINEWIDTH_PCT_DEATHS,
    )
    ax.plot(
        data[constants.COL_DATE],
        data[constants.COL_ROLLING_PCT_DEATHS],
        color=constants.COLOR_ROLLING_AVERAGE,
        linewidth=constants.LINEWIDTH_ROLLING_AVERAGE,
        linestyle=constants.LINESTYLE_ROLLING_AVERAGE,
    )
    ax.axvline(
        pd.Timestamp(constants.HANDWASHING_START),
        color=constants.COLOR_HANDWASHING_START,
        linestyle=constants.LINESTYLE_HANDWASHING_START,
    )
    ax.set_title(
        constants.SUMMARY_CHART_TITLE, fontsize=constants.SUMMARY_HEADING_FONT_SIZE
    )
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter(constants.YEAR_FORMAT))
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
    ax.tick_params(labelsize=constants.SUMMARY_CHART_FONT_SIZE)
    ax.grid(color=constants.GRID_COLOR, linestyle=constants.GRID_LINESTYLE)


def step_6_summary() -> Figure:
    """@brief Draw the headline results of the study (lecture 596).

    @return A figure with the result panel and the monthly series.
    """
    monthly = load_monthly()
    fig, (left, right) = plt.subplots(
        1,
        2,
        figsize=constants.SUMMARY_FIGURE_SIZE,
        dpi=constants.FIGURE_DPI,
        gridspec_kw={"width_ratios": constants.SUMMARY_WIDTH_RATIOS},
    )
    fig.suptitle(
        constants.SUMMARY_TITLE,
        fontsize=constants.SUPTITLE_FONT_SIZE,
        fontweight="bold",
    )
    _draw_summary_panel(left, summary_lines(monthly))
    _draw_summary_series(right, monthly)
    fig.tight_layout()
    return fig


STEPS: dict[str, Callable[[], Figure]] = {
    constants.STEP_1_NAME: step_1_goals,
    constants.STEP_2_NAME: step_2_data_exploration,
    constants.STEP_3_NAME: step_3_clinic_split,
    constants.STEP_4_NAME: step_4_handwashing_effect,
    constants.STEP_5_NAME: step_5_distributions,
    constants.STEP_6_NAME: step_6_summary,
}


def save_all(output_dir: Path = DEFAULT_OUTPUT_DIR) -> list[Path]:
    """@brief Draw every step and save it as a PNG file.

    @param output_dir Folder for the pictures; it is created when missing.
    @return The paths of the files written.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for name, draw in STEPS.items():
        fig = draw()
        path = output_dir / f"{name}.png"
        fig.savefig(path)
        plt.close(fig)
        written.append(path)
    return written


def main() -> None:
    """@brief Command line entry point: write all step pictures."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    for path in save_all(args.out):
        _LOG.info("%s", path)


if __name__ == "__main__":
    main()

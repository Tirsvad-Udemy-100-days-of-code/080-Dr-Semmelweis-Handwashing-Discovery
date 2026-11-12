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

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.axes import Axes  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402

from semmelweis import constants  # noqa: E402
from semmelweis.infrastructure.csv_loader import (  # noqa: E402
    load_monthly,
    load_yearly,
)
from semmelweis.presentation.charts import (  # noqa: E402
    births_and_deaths_chart,
    clinic_overview_chart,
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


STEPS: dict[str, Callable[[], Figure]] = {
    constants.STEP_1_NAME: step_1_goals,
    constants.STEP_2_NAME: step_2_data_exploration,
    constants.STEP_3_NAME: step_3_clinic_split,
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

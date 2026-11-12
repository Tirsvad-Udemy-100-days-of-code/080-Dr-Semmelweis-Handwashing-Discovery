"""@brief Distributions and the test of statistical significance (lecture 595)."""

from typing import NamedTuple

import numpy as np
import numpy.typing as npt
import pandas as pd
from scipy import stats

from semmelweis import constants


class TTestResult(NamedTuple):
    """@brief Outcome of a two-sample t-test.

    @param statistic The t statistic.
    @param p_value Probability of a difference this large if there were none.
    """

    statistic: float
    p_value: float


def add_washing_hands(
    monthly: pd.DataFrame, start: str = constants.HANDWASHING_START
) -> pd.DataFrame:
    """@brief Mark the months from the date handwashing became mandatory.

    @param monthly The monthly table; it is not changed.
    @param start First day of the period after handwashing began.
    @return A copy with the boolean column washing_hands.
    """
    result = monthly.copy()
    result[constants.COL_WASHING_HANDS] = np.where(
        result[constants.COL_DATE] >= pd.Timestamp(start), True, False
    )
    return result


def group_means(marked: pd.DataFrame) -> tuple[float, float]:
    """@brief Mean monthly proportion of deaths without and with handwashing.

    @param marked Table with the columns pct_deaths and washing_hands.
    @return The mean without and the mean with handwashing, as fractions.
    """
    means = marked.groupby(constants.COL_WASHING_HANDS)[constants.COL_PCT_DEATHS].mean()
    return float(means[False]), float(means[True])


def two_sample_t_test(before: pd.Series, after: pd.Series) -> TTestResult:
    """@brief Test whether two groups have the same mean (SciPy ttest_ind).

    @param before Monthly proportions of deaths without handwashing.
    @param after Monthly proportions of deaths with handwashing.
    @return The t statistic and the p-value, as the lecture computes them.
    """
    result = stats.ttest_ind(before, after)
    return TTestResult(float(result.statistic), float(result.pvalue))


def is_significant(p_value: float, alpha: float = constants.SIGNIFICANCE_LEVEL) -> bool:
    """@brief Tell whether a p-value is below the significance level.

    @param p_value The p-value of a test.
    @param alpha Significance level; 0.01 means the 99 percent level.
    @return True when p_value is smaller than alpha.
    """
    return p_value < alpha


def kde_curve(
    values: pd.Series, points: int = constants.KDE_POINTS
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """@brief Kernel density estimate of a sample, limited to its data range.

    @param values The sample.
    @param points Number of evaluation points.
    @return The x values from the sample minimum to maximum and the density.
    """
    grid = np.linspace(values.min(), values.max(), points)
    return grid, stats.gaussian_kde(values)(grid)

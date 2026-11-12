"""@brief Tests for the step pictures."""

from pathlib import Path

from semmelweis import constants
from semmelweis.domain.handwashing import (
    add_pct_deaths_monthly,
    average_rate_before_after,
    improvement_factor,
    split_before_after,
)
from semmelweis.domain.significance import two_sample_t_test
from semmelweis.infrastructure.csv_loader import load_monthly
from semmelweis.presentation import screenshots


def test_step_1_goals_draws_two_tables() -> None:
    """@brief Step 1 draws one axis per table."""
    fig = screenshots.step_1_goals()
    assert len(fig.axes) == 2


def test_step_2_data_exploration_draws_twin_axes() -> None:
    """@brief Step 2 draws the births and deaths chart with two axes."""
    fig = screenshots.step_2_data_exploration()
    assert len(fig.axes) == 2


def test_step_3_clinic_split_draws_three_axes() -> None:
    """@brief Step 3 draws births, deaths and proportion of deaths."""
    fig = screenshots.step_3_clinic_split()
    assert len(fig.axes) == 3


def test_step_4_handwashing_effect_draws_one_axis_with_legend() -> None:
    """@brief Step 4 draws the time series with a legend."""
    fig = screenshots.step_4_handwashing_effect()
    assert len(fig.axes) == 1
    assert fig.axes[0].get_legend() is not None


def test_step_5_distributions_draws_three_axes_with_legends() -> None:
    """@brief Step 5 draws the box plot, the histograms and the KDE."""
    fig = screenshots.step_5_distributions()
    assert len(fig.axes) == 3
    assert fig.axes[1].get_legend() is not None
    assert fig.axes[2].get_legend() is not None


def test_step_6_summary_draws_panel_and_series() -> None:
    """@brief Step 6 draws the result panel and the monthly series."""
    fig = screenshots.step_6_summary()
    assert len(fig.axes) == 2
    assert len(fig.axes[1].lines) >= 2


def test_summary_lines_match_domain_values() -> None:
    """@brief The summary text holds the values the domain computes."""
    monthly = load_monthly()
    before_rate, after_rate = average_rate_before_after(monthly)
    data = add_pct_deaths_monthly(monthly)
    before, after = split_before_after(data)
    result = two_sample_t_test(
        before[constants.COL_PCT_DEATHS], after[constants.COL_PCT_DEATHS]
    )
    text = "\n".join(screenshots.summary_lines(monthly))
    assert f"{before_rate:.2f}%" in text
    assert f"{after_rate:.2f}%" in text
    assert f"{improvement_factor(before_rate, after_rate):.1f}x" in text
    assert f"{result.statistic:.2f}" in text
    assert f"{result.p_value:.2e}" in text


def test_step_6_summary_shows_summary_text() -> None:
    """@brief The figure shows the heading and the result lines."""
    fig = screenshots.step_6_summary()
    texts = [t.get_text() for t in fig.axes[0].texts]
    assert constants.SUMMARY_HEADING in texts
    assert any("t statistic" in t for t in texts)


def test_steps_include_summary() -> None:
    """@brief Step 6 is registered under its name."""
    assert "step-6-summary" in screenshots.STEPS


def test_steps_include_distributions() -> None:
    """@brief Step 5 is registered under its name."""
    assert "step-5-distributions" in screenshots.STEPS


def test_steps_include_handwashing_effect() -> None:
    """@brief Step 4 is registered under its name."""
    assert "step-4-handwashing-effect" in screenshots.STEPS


def test_steps_include_clinic_split() -> None:
    """@brief Step 3 is registered under its name."""
    assert "step-3-clinic-split" in screenshots.STEPS


def test_steps_include_data_exploration() -> None:
    """@brief Step 2 is registered under its name."""
    assert "step-2-data-exploration" in screenshots.STEPS


def test_save_all_writes_one_png_per_step(tmp_path: Path) -> None:
    """@brief save_all writes a non-empty PNG for every step."""
    written = screenshots.save_all(tmp_path)
    assert {p.name for p in written} == {f"{n}.png" for n in screenshots.STEPS}
    assert all(p.stat().st_size > 0 for p in written)

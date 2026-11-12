"""@brief Tests for the step pictures."""

from pathlib import Path

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

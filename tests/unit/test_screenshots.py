"""@brief Tests for the step pictures."""

from pathlib import Path

from semmelweis.presentation import screenshots


def test_step_1_goals_draws_two_tables() -> None:
    """@brief Step 1 draws one axis per table."""
    fig = screenshots.step_1_goals()
    assert len(fig.axes) == 2


def test_save_all_writes_one_png_per_step(tmp_path: Path) -> None:
    """@brief save_all writes a non-empty PNG for every step."""
    written = screenshots.save_all(tmp_path)
    assert {p.name for p in written} == {f"{n}.png" for n in screenshots.STEPS}
    assert all(p.stat().st_size > 0 for p in written)

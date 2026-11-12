"""@brief Tests for the constants and the shipped data files."""

from importlib import resources

from semmelweis import constants


def test_data_files_exist_in_package() -> None:
    """@brief Both CSV files ship inside the package."""
    data = resources.files(constants.DATA_PACKAGE)
    assert data.joinpath(constants.YEARLY_FILE).is_file()
    assert data.joinpath(constants.MONTHLY_FILE).is_file()


def test_clinic_names_are_distinct() -> None:
    """@brief The two clinics have different names."""
    assert constants.CLINIC_1 != constants.CLINIC_2


def test_significance_level_is_one_percent() -> None:
    """@brief The significance level is one percent."""
    assert constants.SIGNIFICANCE_LEVEL == 0.01

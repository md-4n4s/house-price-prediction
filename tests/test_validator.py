import pandas as pd

from src.preprocessing import validator


def test_validate_data() -> None:

    original = pd.DataFrame({"garage_yr_blt": [1870.0, 1999.0, 2007.0, 2026.0, 2261.0]})

    expected = pd.DataFrame({"garage_yr_blt": [1870.0, 1999.0, 2007.0, 2026.0, 2007.0]})

    result = validator.validate_data(original)

    pd.testing.assert_frame_equal(result, expected)

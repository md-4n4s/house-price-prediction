import pandas as pd


def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean invalid data column: garage_yr_blt by replacing invalid data by median"""

    median = df["garage_yr_blt"].median()

    df["garage_yr_blt"] = df["garage_yr_blt"].apply(
        lambda x: x if x <= 2026 else median
    )

    return df

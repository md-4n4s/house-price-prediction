from pathlib import Path

import pandas as pd


def load_data(
    path: Path, date_column: list[str] | None = None, index_col: int | str = 0
) -> pd.DataFrame:

    df = pd.read_csv(path, parse_dates=date_column, index_col=index_col)

    return df

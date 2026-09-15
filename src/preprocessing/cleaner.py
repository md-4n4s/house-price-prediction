import pandas as pd


def standardize_column_names(columns: pd.Index) -> pd.Index:

    columns = columns.str.strip().str.lower().str.replace(" ", "_")

    return columns


def drop_unnecessary_columns(df: pd.DataFrame, columns: list | None) -> pd.DataFrame:

    if columns:
        df.drop(columns=columns, inplace=True)

    return df


def fill_with_mean(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Fill missing values with mean of the column"""

    for column in columns:

        # Missing values of every column are replaced by its own mode
        df[column] = df[column].fillna(df[column].mean())

    return df


def fill_with_none(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Fill missing values with None"""

    df[columns] = df[columns].fillna("None")

    return df


def fill_with_zero(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Fill missing values with 0"""

    df[columns] = df[columns].fillna(0)

    return df


def fill_with_mode(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Fill missing values with mode of the column"""

    for column in columns:

        # Missing values of every column are replaced by its own mode
        df[column] = df[column].fillna(df[column].mode().iloc[0])

    return df


def fill_missing_values(
    df: pd.DataFrame, strategy: dict[str, list[str]]
) -> pd.DataFrame:
    """Fill missing values with requirement of the column"""

    df = fill_with_mean(df, strategy["mean"])
    df = fill_with_none(df, strategy["none"])
    df = fill_with_zero(df, strategy["zero"])
    df = fill_with_mode(df, strategy["mode"])

    return df


def clean_data(
    df: pd.DataFrame,
    strategy: dict[str, list[str]],
    unnecessary_columns: list[str] | None = None,
) -> pd.DataFrame:
    """Clean data by standardizing column names, dropping unnecessary columns, and filling missing values"""

    df.columns = standardize_column_names(df.columns)

    drop_unnecessary_columns(df, unnecessary_columns)

    df = fill_missing_values(df, strategy)

    return df

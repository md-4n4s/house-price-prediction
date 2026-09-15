from cmath import nan

import pandas as pd

from src.preprocessing import cleaner


def test_standardize_column_names() -> None:

    original = pd.Index(["  Order Id ", "Customer nAMe    ", "   pRicE"])

    expected = pd.Index(["order_id", "customer_name", "price"])

    result = cleaner.standardize_column_names(original)

    assert result.equals(expected)


def test_drop_unnecessary_columns() -> None:

    original = pd.DataFrame(columns=["order_id", "customer_name", "price"])

    expected = pd.DataFrame(columns=["order_id", "price"])

    result = cleaner.drop_unnecessary_columns(original, ["customer_name"])

    assert result.equals(expected)


def test_fill_with_mean() -> None:

    original = pd.DataFrame({"marks": [90.0, 100.0, nan, 80.0]})

    result = cleaner.fill_with_mean(original, ["marks"])
    assert result["marks"].tolist() == [90.0, 100.0, 90.0, 80.0]


def test_fill_with_none() -> None:

    original = pd.DataFrame({"marks": ["90", "100", nan, "80"]})

    result = cleaner.fill_with_none(original, ["marks"])
    assert result["marks"].tolist() == ["90", "100", "None", "80"]


def test_fill_with_zero() -> None:

    original = pd.DataFrame({"marks": [90.0, 100.0, nan, 80.0]})

    result = cleaner.fill_with_zero(original, ["marks"])
    assert result["marks"].tolist() == [90.0, 100.0, 0, 80.0]


def test_fill_with_mode() -> None:

    original = pd.DataFrame({"marks": [80.0, 100.0, nan, 80.0]})

    result = cleaner.fill_with_mode(original, ["marks"])
    assert result["marks"].tolist() == [80.0, 100.0, 80.0, 80.0]


def test_fill_missing_values() -> None:

    original = pd.DataFrame(
        {
            "name": ["a", "a", nan],
            "marks": [10.0, nan, 20.0],
            "age": [18, 18, nan],
            "salary": [nan, nan, 50000],
        }
    )

    strategy = {
        "mean": ["marks"],
        "mode": ["age"],
        "none": ["name"],
        "zero": ["salary"],
    }

    expected = pd.DataFrame(
        {
            "name": ["a", "a", "None"],
            "marks": [10.0, 15.0, 20.0],
            "age": [18.0, 18.0, 18.0],
            "salary": [0.0, 0.0, 50000.0],
        }
    )

    result = cleaner.fill_missing_values(original, strategy)

    assert result.equals(expected)


def test_clean_data() -> None:

    original = pd.DataFrame(
        {
            " name ": ["a", "a", nan],
            "mArks": [10.0, nan, 20.0],
            "Age": [18, 18, nan],
            "salARy": [nan, nan, 50000],
            "extra": [nan, nan, nan],
        }
    )

    expected = pd.DataFrame(
        {
            "name": ["a", "a", "None"],
            "marks": [10.0, 15.0, 20.0],
            "age": [18.0, 18.0, 18.0],
            "salary": [0.0, 0.0, 50000.0],
        }
    )

    strategy = {
        "mean": ["marks"],
        "mode": ["age"],
        "none": ["name"],
        "zero": ["salary"],
    }

    result = cleaner.clean_data(original, strategy, ["extra"])

    assert result.equals(expected)

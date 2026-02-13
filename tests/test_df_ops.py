import pytest
from src.df_ops import (
    build_dataframe,
    mean_age,
    mean_salary,
    filter_by_department,
    row_count,
)


def test_build_dataframe_structure():
    df = build_dataframe()
    assert list(df.columns) == ["age", "salaire", "departement"]
    assert len(df) == 8


def test_build_dataframe_types():
    df = build_dataframe()
    assert df["age"].dtype.kind in ("i", "u")
    assert df["salaire"].dtype.kind == "f"
    assert df["departement"].dtype == object


def test_means():
    df = build_dataframe()
    assert mean_age(df) == 34.5
    assert mean_salary(df) == pytest.approx(3775.0)


def test_filter_it():
    df = build_dataframe()
    it_df = filter_by_department(df, "IT")
    assert (it_df["departement"] == "IT").all()
    assert len(it_df) == 4


def test_row_count():
    df = build_dataframe()
    assert row_count(df) == 8

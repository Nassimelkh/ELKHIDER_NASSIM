import pandas as pd


def build_dataframe():
    data = {
        "age": [25, 30, 22, 45, 35, 28, 50, 41],
        "salaire": [2800.0, 3200.0, 2100.0, 5000.0, 3800.0, 2600.0, 6200.0, 4500.0],
        "departement": ["IT", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    }
    df = pd.DataFrame(data)

    # Forcer le type object pour correspondre au test
    df["departement"] = df["departement"].astype(object)

    return df



def mean_age(df):
    if "age" not in df.columns:
        raise ValueError("La colonne 'age' est manquante")
    return df["age"].mean()


def mean_salary(df):
    if "salaire" not in df.columns:
        raise ValueError("La colonne 'salaire' est manquante")
    return df["salaire"].mean()


def filter_by_department(df, dept):
    if "departement" not in df.columns:
        raise ValueError("La colonne 'departement' est manquante")
    return df[df["departement"] == dept]


def row_count(df):
    return len(df)

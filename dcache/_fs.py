import pickle
from typing import Any

import pandas as pd


def save_df(filename: str, file: pd.DataFrame) -> None:
    file.to_parquet(filename + ".parquet")


def load_df(filename: str) -> pd.DataFrame:
    return pd.read_parquet(filename)


def save_to_file(filename: str, file: Any) -> None:
    if isinstance(file, pd.DataFrame):
        save_df(filename=filename, file=file)
        return

    with open(filename + ".pkl", "wb") as f:
        pickle.dump(f, file)


def load_File(filename: str) -> Any:
    extension = filename.split(".")[-1]
    if extension == "parquet":
        df = load_df(filename=filename)
        return df

    with open(filename, "rb") as f:
        file = pickle.load(f)

    return file

import pickle
from typing import Any
from pathlib import Path

import pandas as pd


def save_df(filename: Path, data: pd.DataFrame) -> None:
    data.to_parquet(filename.with_suffix(".parquet"))


def load_df(filename: Path) -> pd.DataFrame:
    return pd.read_parquet(filename)


def save_to_file(filename: Path, data: Any) -> None:
    if isinstance(data, pd.DataFrame):
        save_df(filename=filename, data=data)
        return

    with open(filename.with_suffix(".pkl"), "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def load_file(filename: Path, extension: str) -> Any:
    if extension == "parquet":
        df = load_df(filename=filename)
        return df

    with open(filename, "rb") as f:
        data = pickle.load(f)

    return data

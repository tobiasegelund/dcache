import pickle
import datetime
from typing import Any, Optional
from pathlib import Path

import pandas as pd

from ._exceptions import FileExpired, PathDoesNotExists


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


def scan_cache(
    cache_dir: Path, hash_with_prefix: str, expiration_time: Optional[int]
) -> Any:
    for file in cache_dir.glob("dcache_*"):
        _file = str(file).split("/")[-1]
        _file = _file.split(".")
        filename, extension = _file
        if filename == hash_with_prefix:

            if expiration_time is not None:
                last_minute_seconds = (
                    datetime.datetime.now()
                    - datetime.datetime.fromtimestamp(file.stat().st_mtime)
                ).seconds
                last_modified_minutes = int(last_minute_seconds / 60)
                evalute_expiration_time(
                    current_time=last_modified_minutes, expiration_time=expiration_time
                )

            result = load_file(filename=file, extension=extension)
            return result

    raise FileNotFoundError()


def evalute_expiration_time(current_time: int, expiration_time: int) -> None:
    if current_time < expiration_time:
        return

    raise FileExpired()

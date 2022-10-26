from pathlib import Path
import tempfile


def find_tmp_directory() -> Path:
    path = tempfile.gettempdir()
    return Path(path)


def convert_str_to_path(path: str) -> Path:
    if not isinstance(path, str):
        raise ValueError(f"{path} is not a str but {type(path)}")
    return Path(path)


def create_dir_if_not_exists(path: Path) -> None:
    if not path.exists():
        path.mkdir()

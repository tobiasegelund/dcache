from pathlib import Path
import tempfile


def find_tmp_directory() -> Path:
    path = tempfile.gettempdir()
    return Path(path)

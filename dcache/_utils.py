import tempfile
import inspect
import hashlib
from typing import Callable, Optional
from pathlib import Path


def find_tmp_directory() -> Path:
    path = tempfile.gettempdir()
    return Path(path)


def is_method(func: Callable):
    spec = inspect.signature(func)
    if len(spec.parameters) > 0:
        if list(spec.parameters.keys())[0] in ("cls", "self"):
            return True
    return False


def hash_string(name: str, length: Optional[int] = None) -> str:
    if length is not None:
        return hashlib.md5(name.encode("utf-8")).hexdigest()[:length]
    return hashlib.md5(name.encode("utf-8")).hexdigest()

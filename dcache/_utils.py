import hashlib
from io import StringIO, BytesIO
from typing import Callable, Optional
import joblib


def prefix_filename(filename: str, prefix: str = "dcache_") -> str:
    return prefix + filename


def hash_string(name: str, length: Optional[int] = None) -> str:
    if length is not None:
        return hashlib.md5(name.encode("utf-8")).hexdigest()[:length]
    return hashlib.md5(name.encode("utf-8")).hexdigest()


def create_input_hash_values(*args, **kwargs) -> str:
    # TODO: Handle objects with __dict__, and other data types in specific way, including a default way
    hash_values = ""
    for arg in args:
        hash_values += joblib.hash(arg)

    for _, val in kwargs.items():
        hash_values += joblib.hash(val)

    return hash_values


def hash_input(*args, **kwargs) -> str:
    input = create_input_hash_values(*args, **kwargs)
    return hash_string(input)

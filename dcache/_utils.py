import hashlib
from io import StringIO, BytesIO
from typing import Callable, Optional


def prefix_filename(filename: str, prefix: str = "dcache_") -> str:
    return prefix + filename


def hash_string(name: str, length: Optional[int] = None) -> str:
    if length is not None:
        return hashlib.md5(name.encode("utf-8")).hexdigest()[:length]
    return hashlib.md5(name.encode("utf-8")).hexdigest()


def input_to_string(*args, **kwargs) -> str:
    # TODO: Handle objects with __dict__, and other data types in specific way, including a default way
    name = ""
    for arg in args:
        name += str(arg)

    for _, val in kwargs:
        name += str(val)

    return name


def hash_input(*args, **kwargs) -> str:
    input = input_to_string(*args, **kwargs)
    return hash_string(input)

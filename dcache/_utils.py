import inspect
import hashlib
from io import StringIO, BytesIO
from typing import Callable, Optional


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

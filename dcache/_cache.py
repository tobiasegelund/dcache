from pathlib import Path
from typing import Callable, Optional, Union
from functools import wraps, partial

from ._adaptor import auto_adapt_to_methods


def dcache(
    func: Optional[Callable] = None, path: Optional[Union[str, Path]] = None
) -> Callable:
    """Cache to output to disk

    The decorator hashes the input and maps the serialized output to hashed value on disk.

    params:
        path, str | Path, default=/tmp: The path of the directory where cache are stored
    """

    @auto_adapt_to_methods
    def wrapper(func: Callable, *args, **kwargs):
        result = func(*args, **kwargs)

        return result

    if func is not None:
        if not callable(func):
            raise ValueError()
        return wraps(func)(partial(wrapper, func))

    def wrap_callable(func: Callable) -> Callable:
        return wraps(func)(partial(wrapper, func))

    return wrap_callable

from pathlib import Path
from typing import Callable, Optional, Union
from functools import wraps, partial

from ._adaptor import auto_adapt_to_methods
from ._os import find_tmp_directory

# from ._utils import


def dcache(
    func: Optional[Callable] = None,
    path: Optional[Union[str, Path]] = None,
    expiration_time: Optional[int] = None,
    save_hash_values_in_memory: bool = False,
) -> Callable:
    """Cache output to disk

    The decorator hashes the input and maps the serialized output to hashed value on disk.

    params:
        path, str|Path, default=/tmp: The path of the directory where cache are stored
        expiration_time, int, default=None: The expiration time in seconds
        save_hash_values_in_memory, bool, default=False:
    """

    cache_dir = find_tmp_directory() if path is None else path

    if not isinstance(cache_dir, Path):
        cache_dir = Path(cache_dir)

    @auto_adapt_to_methods
    def wrapper(func: Callable, *args, **kwargs):
        # TODO:
        # 1. Create hash value
        # 2. Lookup hash value in directory
        # 3. Load data or run func

        result = func(*args, **kwargs)

        return result

    if func is not None:
        if not callable(func):
            raise ValueError()
        return wraps(func)(partial(wrapper, func))

    def wrap_callable(func: Callable) -> Callable:
        return wraps(func)(partial(wrapper, func))

    return wrap_callable

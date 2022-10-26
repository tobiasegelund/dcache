from pathlib import Path
from typing import Callable, Optional, Union
from functools import wraps, partial

from ._adaptor import auto_adapt_to_methods
from ._os import find_tmp_directory, convert_str_to_path
from ._utils import hash_input
from ._fs import load_file, save_to_file


def dcache(
    func: Optional[Callable] = None,
    path: Optional[Union[str, Path]] = None,
    expiration_time: Optional[int] = None,
) -> Callable:
    """Cache output to disk

    The decorator hashes the input and maps the serialized output to hashed value on disk.

    params:
        path, str|Path, default=None: The path of the directory where cache are stored.
            If None it uses the default tmp directory of the operating system
        expiration_time, int, default=None: The expiration time in seconds
    """

    cache_dir = find_tmp_directory() if path is None else path

    if not isinstance(cache_dir, Path):
        cache_dir = convert_str_to_path(cache_dir)

    @auto_adapt_to_methods
    def wrapper(func: Callable, *args, **kwargs):
        result = None
        hash_value = hash_input(func=func, *args, **kwargs)

        for file in cache_dir.glob("dcache_*"):
            file = str(file).split("/")[-1]
            file = file.split(".")
            filename, extension = file
            if filename == hash_value:
                result = load_file(filename=filename, extension=extension)

        if result is None:
            result = func(*args, **kwargs)
            save_to_file(filename=hash_value, file=result)

        return result

    if func is not None:
        if not callable(func):
            raise ValueError()
        return wraps(func)(partial(wrapper, func))

    def wrap_callable(func: Callable) -> Callable:
        return wraps(func)(partial(wrapper, func))

    return wrap_callable


def clear_dcache(path: Optional[Union[str, Path]] = None):
    cache_dir = find_tmp_directory() if path is None else path

    if not isinstance(cache_dir, Path):
        cache_dir = convert_str_to_path(cache_dir)

    for file in cache_dir.glob("dcache_*"):
        file.unlink()

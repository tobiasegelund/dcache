from pathlib import Path
from typing import Callable, Optional, Union
from functools import wraps, partial

from ._adaptor import auto_adapt_to_methods
from ._os import find_tmp_directory, convert_str_to_path
from ._utils import hash_input, prefix_filename, ismethod
from ._fs import look_up_file_in_cache, save_to_file
from ._exceptions import NothingToReturn, FileExpired


def dcache(
    func: Optional[Callable] = None,
    *,
    cache_dir: Optional[Union[str, Path]] = None,
    expiration_time: Optional[int] = None,
) -> Callable:
    """Cache output to disk

    The decorator hashes the input and maps the serialized output to hashed value on disk.

    params:
        cache_dir, str|Path, default=None: The path of the directory where cache are stored.
            If None it uses the default tmp directory of the operating system
        expiration_time, int, default=None: The expiration time in minutes
    """

    cache_dir = find_tmp_directory() if cache_dir is None else cache_dir

    if not isinstance(cache_dir, Path):
        cache_dir = convert_str_to_path(cache_dir)

    # TODO: Fix logic to handle methods as well without comprising decorator call with or without ()
    # @auto_adapt_to_methods
    def wrapper(func: Callable, *args, **kwargs):
        result = None
        hash_value = hash_input(func=func.__qualname__, *args, **kwargs)
        hash_value_with_prefix = prefix_filename(filename=hash_value)

        # TODO: Split the moves up here into fewer funcs and use exceptions to try/catch

        try:
            result = look_up_file_in_cache(
                cache_dir=cache_dir,
                hash_value_with_prefix=hash_value_with_prefix,
                expiration_time=expiration_time,
            )
        except (FileNotFoundError, FileExpired):
            pass

        if result is None:
            result = func(*args, **kwargs)

            if result is None:
                raise NothingToReturn(f"{func} doesn't return anything")

            save_to_file(
                filename=cache_dir.joinpath(hash_value_with_prefix), data=result
            )

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

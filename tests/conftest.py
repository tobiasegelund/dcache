import pytest

from dcache._os import find_tmp_directory


@pytest.fixture
def tmp_path():
    yield find_tmp_directory()

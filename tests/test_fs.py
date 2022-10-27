# from pathlib import Path
from dcache._fs import save_to_file, load_file


def test_save_to_file(tmp_path):
    save_to_file(filename=tmp_path.joinpath("test_save_to_file"), data=2)


def test_load_file():
    pass

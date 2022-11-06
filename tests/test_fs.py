import pytest
from dcache._fs import save_to_file, load_file

import pandas as pd


def test_save_to_file(tmp_path):
    save_to_file(filename=tmp_path.joinpath("test_save_to_file"), data=2)


def test_save_to_file_w_df(tmp_path):
    save_to_file(filename=tmp_path.joinpath("test_save_to_file"), data=pd.DataFrame())


def test_load_file():
    pass

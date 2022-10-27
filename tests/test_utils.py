import pytest
from dcache._utils import prefix_filename, hash_input, ismethod


def test_prefix_filename():
    new_name = prefix_filename(filename="name", prefix="dcache_")

    assert new_name == "dcache_name"


def test_hash_input():
    hash_value = hash_input("ja", 2, 2, a=2, b=4)

    assert hash_value == "bb2fc93facbddb3ac7bb7181dae1f743"


# def test_ismethod():
#     class TestMethod:
#         def method(self):
#             pass

#     def function():
#         pass

#     assert ismethod(TestMethod.method) == True
#     assert ismethod(function) == False

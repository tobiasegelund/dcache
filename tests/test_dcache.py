import pytest
from dcache import dcache
from dcache._exceptions import NothingToReturn


# def test_method_with_parenthesis():
#     class TestMethod:
#         @dcache()
#         def test_method(self):
#             pass

#     with pytest.raises(NothingToReturn) as exc_info:
#         TestMethod().test_method()


# def test_method_without_parenthesis():
#     class TestMethod:
#         @dcache
#         def test_method(self):
#             pass

#     with pytest.raises(NothingToReturn) as exc_info:
#         TestMethod().test_method()


def test_func_without_parenthesis():
    @dcache
    def test_func():
        pass

    with pytest.raises(NothingToReturn) as exc_info:
        test_func()


def test_func_with_parenthesis():
    @dcache()
    def test_func():
        pass

    with pytest.raises(NothingToReturn) as exc_info:
        test_func()

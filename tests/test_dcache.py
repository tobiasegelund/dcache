from dcache import dcache


def test_method_with_parenthesis():
    class TestMethod:
        @dcache()
        def test_method(self):
            pass

    TestMethod().test_method()


def test_method_without_parenthesis():
    class TestMethod:
        @dcache
        def test_method(self):
            pass

    TestMethod().test_method()


def test_func_without_parenthesis():
    @dcache
    def test_func():
        pass

    test_func()


def test_func_with_parenthesis():
    @dcache()
    def test_func():
        pass

    test_func()

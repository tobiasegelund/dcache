from typing import Callable


class _MethodDecoratorAdaptor(object):
    def __init__(self, decorator: Callable, func: Callable):
        self.decorator = decorator
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.decorator(self.func)(*args, **kwargs)

    def __get__(self, instance, owner):
        return self.decorator(self.func.__get__(instance, owner))


def auto_adapt_to_methods(decorator: Callable):
    def adapt(func):
        return _MethodDecoratorAdaptor(decorator, func)

    return adapt

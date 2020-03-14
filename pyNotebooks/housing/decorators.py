"""
Helpful decorators for the housing project.
"""

import functools


def showChange(func):
    """ Show dimension change when filtering"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        print('{}()\n\t{}: {} -> {}'.format(
              func.__name__,
              func.__doc__, 
              args[0].shape, 
              rv.shape))

        return rv
    return wrapper


def pShape(func):
    """ Print the shape of the return value"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        print('{}()\n\t{}: {}'.format(func.__name__, func.__doc__, rv.shape))
        return rv
    return wrapper


def pDoc(func):
    """ Print the docstring of a function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        print('{}'.format(func.__doc__))
        return rv
    return wrapper
__doc__ = """Partial evaluation
"""
from functools import partial


def power(a, n):
    return a ** n


if __name__ == "__main__":
    square = partial(power, n=2)

    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

    cube = partial(power, n=3)

    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(4) == 64

__doc__ = """Closures in Python

A CLOSURE is a function object that remembers values in enclosing scopes
regardless of whether those scopes are still present in memory. If you
have ever written a function that returned another function, you probably
may have used closures even without knowing about them.
"""


def power(n):
    def closure(a):
        return a ** n

    return closure


if __name__ == "__main__":
    square = power(2)
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

    assert square.__closure__[0].cell_contents == 2
    assert id(power(2)) == id(power(2)) == id(power(2)) == id(power(2))
    assert id(power(3)) == id(power(3)) == id(power(3)) == id(power(3))

    cube = power(3)

    # Closure's magic
    assert 'power' in dir()
    del power
    assert not 'power' in dir()

    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(4) == 64

    assert cube.__closure__[0].cell_contents == 3

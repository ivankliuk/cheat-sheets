__doc__ = """
Decorator functions examples.
"""

from time import time as time


def timer(f):
    """A decorator function for counting execution time"""

    def wrap(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        stop = time() - start
        print "Execution time {0} ms.".format(stop * 1000)
        return result

    return wrap


@timer
def fib(n):
    """Fibonacci numbers function (using loop)"""
    x, y = 1, 1
    for i in range(n - 1):
        x, y = y, x + y

    return x


print fib(20)

# TODO: Improve decorator for calling decorated function recursively
@timer
def fib(n):
    """Fibonacci numbers function (using recursion)"""
    if n == 1 or n == 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)


print fib(20)

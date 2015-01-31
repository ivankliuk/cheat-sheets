__doc__ = """
Itertools module - Functions creating iterators for efficient looping.
"""
import itertools

# Infinite Iterators

def count(start=0, step=1):
    """count(5, 2) -> 5 7 9 11 13 ..."""
    n = start
    while True:
        yield n
        n += step


def cycle(iterable):
    """cycle([1, 2, 3]) -> 1 2 3 1 2 ..."""
    while True:
        for element in iterable:
            try:
                yield element
            except StopIteration:
                cycle(iterable)


def repeat(obj, times=None):
    """repeat('x', 5) -> 'x' 'x' x' 'x' 'x'
       repeat('x') -> 'x' 'x' 'x' 'x' 'x' ...
    """
    if times:
        called = 0
        while times > called:
            yield obj
            called += 1
    else:
        while True:
            yield obj


# Iterators terminating on the shortest input sequence:

def chain(*iterables):
    """chain('XYZ, [1, 2, 3]) -> X Y Z 1 2 3"""
    for it in iterables:
        for element in it:
            yield element

# Tests
if __name__ == '__main__':
    # itertools.count
    cnt = count(5, 2)
    iter_cnt = itertools.count(5, 2)
    assert [cnt.next() for i in range(5)] == [iter_cnt.next() for i in range(5)]

    # itertools.cycle
    s = 'String is an iterator too!'
    cyc = cycle(s)
    iter_cyc = itertools.cycle(s)
    assert [cyc.next() for i in range(100)] == [iter_cyc.next() for i in range(100)]

    # itertools.repeat
    rep = repeat('x', 5)
    iter_rep = itertools.repeat('x', 5)
    assert [rep.next() for i in range(5)] == [iter_rep.next() for i in range(5)]

    rep = repeat('x')
    iter_rep = itertools.repeat('x')
    assert [rep.next() for i in range(10)] == [iter_rep.next() for i in range(10)]

    # itertools.chain
    iter_1 = 'XYZ'
    iter_2 = [1, 2, 3]
    ch = chain(iter_1, iter_2)
    iter_ch = itertools.chain(iter_1, iter_2)
    assert [ch.next() for i in range(6)] == [iter_ch.next() for i in range(6)]

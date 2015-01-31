__doc__ = """Iterator interface in Python
"""


class Iter(object):
    def __init__(self, lst_obj):
        self.list_obj = list(lst_obj)

    def __iter__(self):
        return self

    def next(self):
        try:
            return self.list_obj.pop(0)
        except IndexError:
            raise StopIteration


class Container(object):
    """Container class which exposes different
    approaches in implementation of iterator
    """

    def __init__(self, lst_obj):
        self.lst_obj = lst_obj

    def proxy_iter(self):
        return iter(self.lst_obj)

    def custom_iter(self):
        return Iter(self.lst_obj)

    def generator_iter(self):
        for i in self.lst_obj:
            yield i


# Tests
if __name__ == "__main__":
    lst = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    container = Container(lst)

    proxy_iter = [i for i in container.proxy_iter()]
    custom_iter = [i for i in container.custom_iter()]
    generator_iter = [i for i in container.generator_iter()]

    assert proxy_iter == custom_iter == generator_iter

    # Whether object is iterable
    import collections

    assert isinstance(proxy_iter, collections.Iterable)
    assert isinstance(custom_iter, collections.Iterable)
    assert isinstance(generator_iter, collections.Iterable)

__doc__ = """Magic methods
"""
import doctest


class Talker(object):
    """
    >>> talker = Talker()
    >>> talker.say("Hello!")
    'Hello!'
    >>> talker.scream("Hey!")
    'Hey!'
    >>> talker.whine("I want candy!")
    'I want candy!'
    >>> talker = Talker()
    >>> talker.whistle("La-la-la!")
    Traceback (most recent call last):
      ...
    AttributeError: I know only how to say, scream or whine!
    """

    def _do_action(self, phrase):
        return phrase

    def __getattr__(self, item):
        if item in ('say', 'scream', 'whine'):
            return self._do_action
        raise AttributeError("I know only how to say, scream or whine!")


class Meta(type):
    def _do_action(cls, phrase):
        return phrase

    def __getattr__(cls, item):
        if item in ('say', 'scream', 'whine'):
            return cls._do_action
        raise AttributeError("I know only how to say, scream or whine!")


class CTalker(object):
    """
    >>> talker = CTalker
    >>> talker.say("Hello!")
    'Hello!'
    >>> talker.scream("Hey!")
    'Hey!'
    >>> talker.whine("I want candy!")
    'I want candy!'
    >>> talker = Talker()
    >>> talker.whistle("La-la-la!")
    Traceback (most recent call last):
      ...
    AttributeError: I know only how to say, scream or whine!
    """

    __metaclass__ = Meta


if __name__ == "__main__":
    doctest.testmod()

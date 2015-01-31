__doc__ = """
Object oriented programming basics in Python
"""
import doctest


class StaticTalker(object):
    """
    staticmethod(function) converts a function to be a static method.
    A static method does not receive an implicit first argument.
    It is not necessary to instantiate the class for invoking static methods.
    """

    def welcome_msg(self):
        """
        A regular method cannot be called without instantiation of the class.

        >>> StaticTalker.welcome_msg()
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: unbound method welcome_msg() must be called with StaticTalker instance as first argument (got nothing instead)
        >>> StaticTalker().welcome_msg()
        Hello! I'm a method.
        >>> t = StaticTalker()
        >>> StaticTalker.welcome_msg(t)
        Hello! I'm a method.
        """
        print u"Hello! I'm a method."

    @staticmethod
    def good_day_msg():
        """
        Static methods can.

        >>> StaticTalker.good_day_msg()
        Isn't it a good day? I'm a static method. I was decorated.
        >>> StaticTalker.how_are_u_msg()
        How are you today? I'm a static method. I was passed as an argument.
        """
        print u"Isn't it a good day? I'm a static method. I was decorated."

    def how_are_u_msg():
        print u"How are you today? I'm a static method. I was passed as an argument."

    how_are_u_msg = staticmethod(how_are_u_msg)


class ClassTalker(object):
    """
    classmethod(function) converts a function to be a class method.

    A class method receives the class as implicit first argument,
    just like an instance method receives the instance.
    """

    @classmethod
    def good_day_msg(cls):
        """
        Static methods can be called without instantiation of the class
        as well as static methods.

        >>> ClassTalker.good_day_msg()
        I'm wishing you a great day! I'm a class method. I was decorated.
        """
        print (u"I'm wishing you a great day! I'm a class method. "
               u"I was decorated.")

    def my_name_msg(cls):
        """
        The first argument of the classmethod is accessible withing the method.

        >>> ClassTalker.my_name_msg()
        My name is ClassTalker! I'm a class method. I was passed as an argument.
        """
        print (u"My name is {0}! I'm a class method. "
               u"I was passed as an argument.".format(cls.__name__))

    my_name_msg = classmethod(my_name_msg)


if __name__ == "__main__":
    doctest.testmod()

#   doctests
#   - we can write tests for functions inside of the docstring
#   - we need to run --> python3 -m doctest -v 2_doctest.py

#   example 1
def add(x, y):
    """add together x and y
    >>> add(1,2)
    3
    >>> add(10,20)
    30
    """
    return x + y

#

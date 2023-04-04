# Python internal representation of Scheme Expressions

class LinkedList(object):
    """A LinkedList has two instance attributes: first and rest.

    >>> s = LinkedList(1, LinkedList(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """

    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __repr__(self):
        return 'LinkedList({0}, {1})'.format(repr(self.first), repr(self.rest))

    def __str__(self):
        s = "(" + str(self.first)
        rest = self.rest
        while isinstance(rest, LinkedList):
            s += " " + str(rest.first)
            rest = rest.rest
        if rest is not nil:
            s += " . " + str(rest)
        return s + ")"

    def __len__(self):
        n, rest = 1, self.rest
        while isinstance(rest, LinkedList):
            n += 1
            rest = rest.rest
        if rest is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        lst = self
        for _ in range(k):
            if lst.rest is nil:
                raise IndexError("list index out of bounds")
            elif not isinstance(lst.rest, LinkedList):
                raise TypeError("ill-formed list")
            lst = lst.rest
        return lst.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.rest is nil or isinstance(self.rest, LinkedList):
            return LinkedList(mapped, self.rest.map(fn))
        else:
            raise TypeError("ill-formed list")


class nil(object):
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self


nil = nil()  # Assignment hides the nil class; there is only one instance


# Scheme list parser


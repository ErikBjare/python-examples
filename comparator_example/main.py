from random import randint

class ComparableThing:
    """Represents a number, but sorts in reverse order"""

    def __init__(self, i):
        self.i = i

    def __lt__(self, other):
        """The less-than operator"""
        return self.i > other.i

    def __repr__(self):
        return "<num " + str(self.i) + ">"

l = [ComparableThing(randint(0, 10)) for _ in range(10)]
print("Unsorted:         " + str(l))
print("Sorted:           " + str(sorted(l)))
print("Reversely sorted: " + str(sorted(l, reverse=True)))

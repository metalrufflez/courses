class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self,another):
        """Intersect two intSets, returns a intSet with elements in ocmmon
           Return empty list if no element in common"""
        intersected = intSet()

        for element in self.vals:
            if another.member(element):
                intersected.insert(element)

        return intersected

    def __len__(self):
        """Helper for len function"""
        return len(self.vals)

s1 = intSet()
s1.insert(1)
s1.insert(2)
s1.insert(3)

s2 = intSet()
s2.insert(2)
s2.insert(3)
s2.insert(4)

print s2.intersect(s1)

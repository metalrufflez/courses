class Queue(object):
    """Simple implementation of a FIFO queue"""

    def __init__(self):
        self.vals = []

    def insert(self,x):
        """Insert Values on queue"""
        self.vals.insert(0,x)

    def remove(self):
        """Pops the last element"""
        if len(self.vals) == 0:
            raise ValueError()
        else:
            return self.vals.pop()

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()
queue.insert(7)
print queue.remove()
print queue.remove()
print queue.remove()



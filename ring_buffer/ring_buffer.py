class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):

        if len(self.storage) > self.capacity:
            self.storage.append(item)
            self.storage.pop(0)

    def get(self):
        l = []
        for el in self.storage:
            l.append(el)
        return l

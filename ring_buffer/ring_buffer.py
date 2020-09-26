class RingBuffer:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.buffer = []
        self.index = 0

    def append(self, item):

        if len(self.buffer) < self.capacity:
            # Need to add Item
            self.buffer.append(item)
        else:
            # replace first item and subtract
            self.buffer[self.index] = item
            if self.index == self.capacity - 1:
                self.index = 0
            else:
                self.index += 1

    def get(self):
        return self.buffer

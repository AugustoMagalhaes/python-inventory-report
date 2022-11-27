from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        data, index = self.data, self.index
        if index >= len(data):
            raise StopIteration()
        elemento = data[index]
        self.index += 1
        return elemento

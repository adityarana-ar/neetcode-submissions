class DynamicArray:
    # self.capacity = 0
    # self.arr = None
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0
    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if not self.arr[i]:
            self.size += 1
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return value

    def resize(self) -> None:
        self.arr = self.arr + [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
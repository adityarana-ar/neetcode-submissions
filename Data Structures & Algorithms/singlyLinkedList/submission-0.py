class LinkedList:
    
    def __init__(self):
        self.arr = []
    
    def get(self, index: int) -> int:
        if index >= 0 and index < len(self.arr):
            return self.arr[index]
        return -1

    def insertHead(self, val: int) -> None:
        self.arr = [val] + self.arr
        

    def insertTail(self, val: int) -> None:
        self.arr.append(val)

    def remove(self, index: int) -> bool:
        if index >= 0 and index < len(self.arr):
            self.arr = self.arr[:index] + self.arr[index+1:]
            return True
        return False

    def getValues(self) -> List[int]:
        return self.arr

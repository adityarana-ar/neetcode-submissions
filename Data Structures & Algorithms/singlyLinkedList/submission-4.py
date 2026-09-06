class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head
        self.head = new

        if not self.tail:
            self.tail = new
        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.tail:
            self.tail = self.head = node

        else:
            self.tail.next = node
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if index < 0 or not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        
        curr = self.head
        i = 0

        for _ in range(index - 1):
            if not curr.next:
                return False
            curr = curr.next
        
        if not curr.next:
            return False

        if curr.next == self.tail:
            self.tail = curr
        
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        result = []

        curr = self.head

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        result = ListNode(head.val, None)

        while head.next:
            curr = ListNode(head.next.val, result)
            result = curr
            head = head.next
        
        return result
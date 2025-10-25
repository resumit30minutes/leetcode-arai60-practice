# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        low = head
        fast = head

        while fast is not None and fast.next is not None:
            low = low.next
            fast = fast.next.next

            if low == fast:
                return True
            
        return False
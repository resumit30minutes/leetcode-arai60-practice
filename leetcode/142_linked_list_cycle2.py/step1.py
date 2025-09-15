# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while True:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        
        result = head
        while result != slow:
            result = result.next
            slow = slow.next

        return result
    

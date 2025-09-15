# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         curr1 = head
#         while curr1 is not None:
#             curr2 = head
#             while curr2 is not None:
#                 if curr1.next == curr2:
#                     return True
#                 curr2 


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # while fast.next is not None or fast.next.next is not None:
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
        

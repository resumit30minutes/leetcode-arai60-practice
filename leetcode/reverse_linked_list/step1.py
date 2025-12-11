
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node is not None:
            stack.append(node)
            node = node.next

        if not stack:
            return None

        new_head = stack.pop()
        node = new_head
        while stack:
            node.next = stack.pop()
            node = node.next
        node.next = None

        return new_head


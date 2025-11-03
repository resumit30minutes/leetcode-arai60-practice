from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deletDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        dummy = ListNode()
        prev_node = dummy

        while current_node:
            if prev_node is not dummy and current_node.val == prev_node.val:
                prev_node.next = None
                current_node = current_node.next
                continue

            prev_node.next = current_node

            prev_node = current_node
            current_node = current_node.next

        return dummy.next

        

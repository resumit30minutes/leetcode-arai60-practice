from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
                continue

            node = node.next

        return head


    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        """
        再帰での解法
        """
        return self._skip_duplicates(head, None)

    def _skip_duplicates(self, node: Optional[ListNode], value_to_skip: Optional[int]) -> Optional[ListNode]:
        if node is None:
            return None

        if node.val != value_to_skip:
            node.next = self._skip_duplicates(node.next, node.val)
            return node
        else:
            return self._skip_duplicates(node.next, value_to_skip)



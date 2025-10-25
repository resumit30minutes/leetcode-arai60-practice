from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        setを使って解きなおし
        """
        visited_node_set = set()
        curr_node = head
        while curr_node:
            if curr_node in visited_node_set:
                return True
            
            visited_node_set.add(curr_node)
            curr_node = curr_node.next
        
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        """
        フロイトのアルゴリズム

        一応書き直してみた
        """
        low = head
        fast = head

        while fast and fast.next:
            low = low.next
            fast = fast.next.next

            if low is fast:
                return True
            
        return False

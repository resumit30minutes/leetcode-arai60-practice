from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current_node = head

        while current_node:
            if current_node in visited_nodes:
                return True

            visited_nodes.add(current_node)
            current_node = current_node.next
        
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        """
        フロイドの循環検出法を使った解法
        タイポがあったので再度解き直し
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
            
        return False

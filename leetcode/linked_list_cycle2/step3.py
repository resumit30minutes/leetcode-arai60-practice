from typing import Optional 

class ListNode:
     def __init__(self, v):
         self.val = v
         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        node = head

        while node:
            if node in visited_nodes:
                return node

            visited_nodes.add(node)
            node = node.next

        return None

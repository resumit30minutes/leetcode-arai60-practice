from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        reversed_head = head
        node = head.next
        reversed_head.next = None
        while node is not None:
            tmp = node.next
            node.next = reversed_head
            reversed_head = node
            
            node = tmp
            
        return reversed_head
            

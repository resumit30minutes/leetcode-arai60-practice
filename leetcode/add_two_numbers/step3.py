from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]): Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            total = l1_val + l2_val + carry
            node.next = ListNode(total % 10)
            node = node.next
            carry = total // 10

            l1 = l1 if l1 is not None else None 
            l2 = l2 if l2 is not None else None 

        return dummy.next

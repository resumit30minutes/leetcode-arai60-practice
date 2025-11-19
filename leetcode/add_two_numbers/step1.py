from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        carry = 0

        dummy = ListNode()
        node = dummy
        while node1 is not None or node2 is not None:
            node.next = ListNode()
            node = node.next

            number1 = node1.val if node1 is not None else 0
            number2 = node2.val if node2 is not None else 0
            added = number1 + number2 + carry

            if added >= 10:
                added = added - 10
                carry = 1
            else:
                carry = 0

            node.val = added
            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None

        if carry > 0:
            node.next = ListNode(carry)

        return dummy.next

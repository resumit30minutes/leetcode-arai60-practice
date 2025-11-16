from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        node = head

        while node is not None and node.next is not None:
            if node.val != node.next.val:
                tail = node
                node = node.next
                continue

            value_to_remove = node.val
            while node is not None and node.val == value_to_remove:
                node = node.next
            tail.next = node

        return dummy.next



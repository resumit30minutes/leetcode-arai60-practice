from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = head
        tail = dummy

        while node is not None and node.next is not None:
            value_to_remove = node.val
            if node.next.val != value_to_remove:
                tail = node
                node = node.next
                continue

            # 重複したノードをすべて削除
            while node.next is not None and node.next.val == value_to_remove:
                node = node.next
            tail.next = node

        return dummy.next


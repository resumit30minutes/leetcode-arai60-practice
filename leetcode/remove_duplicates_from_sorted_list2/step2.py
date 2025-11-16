from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = head
        tail = dummy

        while node is not None and node.next is not None:
            if node.val != node.next.val:
                tail = node
                node = node.next
                continue

            # 重複したノードをすべて削除して繋ぎ直す
            value_to_remove = node.val
            while node is not None and node.val == value_to_remove:
                node = node.next
            tail.next = node

        return dummy.next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        入れ替え済みのリストの一番後ろと、次につなげてやるべきノードをもらう
        引き継ぎ相手に投げるノードを確保してから、リストの一番後ろに繋ぎ直して終わり
        """
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

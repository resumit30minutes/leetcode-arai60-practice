from typing import Optional

 # Definition for singly-linked list.
class ListNode:
     def __init__(self, v):
         self.val = v
         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes = set()
        current_node = head

        while current_node:
            if current_node in visited_nodes:
                return current_node

            visited_nodes.add(current_node)
            current_node = current_node.next

        return None


    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        meeting_point = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                meeting_point = fast
                break

        if meeting_point is None:
            return None

        slow = head
        fast = meeting_point
        # 1. slowをheadに戻して前進
        # 2. fastをmeeting_pointから前進
        # この2つの操作を同時に繰り返して、交差した箇所がサイクルの開始地点
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return fast


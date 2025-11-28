from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy.next



    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        再帰での書き方(下のリンクを読んでから見ずに再現してみた)
        https://discord.com/channels/1084280443945353267/1196472827457589338/1197166381146329208
        """
        return self.addTwoNumbersHelper(l1, l2, 0)

    def addTwoNumbersHelper(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None
        
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        node = ListNode(total % 10)
        new_carry = total // 10

        new_l1 = l1.next if l1 else None
        new_l2 = l2.next if l2 else None

        node.next = self.addTwoNumbersHelper(new_l1, new_l2, new_carry)
        return node
        
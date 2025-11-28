from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result_node = dummy
        carry = 0
        node1 = l1
        node2 = l2
        
        while node1 is not None or node2 is not None or carry != 0:
            node1_val = 0
            if node1 is not None:
                node1_val = node1.val
                node1 = node1.next
            
            node2_val = 0
            if node2 is not None:
                node2_val = node2.val
                node2 = node2.next
                
            total = node1_val + node2_val + carry
            result_node.next = ListNode(total % 10)
            result_node = result_node.next
            carry = total // 10
            
        return dummy.next
            
    
    
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        再帰
        """
        dummy = ListNode()
        self.add_two_numbers_helper(l1, l2, 0, dummy)
        return dummy.next
        
    def add_two_numbers_helper(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int, calculated_tail: ListNode):
        if not l1 and not l2 and carry == 0:
            return
        
        l1_node = l1
        l2_node = l2
        total = carry
        
        if l1_node is not None:
            total += l1_node.val
            l1_node = l1_node.next
            
        if l2_node is not None:
            total += l2_node.val
            l2_node = l2_node.next
            
        new_node = ListNode(total % 10, None)
        calculated_tail.next = new_node
        calculated_tail = new_node
        new_carry = total // 10
        
        return self.add_two_numbers_helper(l1_node, l2_node, new_carry, calculated_tail)

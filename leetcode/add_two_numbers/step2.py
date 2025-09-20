
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        carry = 0
        dummy = ListNode()
        result_curr = dummy
        while l1_curr or l2_curr or carry:
            l1_val = l1_curr.val if l1_curr else 0
            l2_val = l2_curr.val if l2_curr else 0
            calc_result = l1_val + l2_val + carry

            if calc_result >= 10:
                calc_result %= 10
                carry = 1
            else:
                carry = 0
            
            result_curr.next = ListNode(calc_result)
            result_curr = result_curr.next

            l1_curr = l1_curr.next if l1_curr else None
            l2_curr = l2_curr.next if l2_curr else None
        

        return dummy.next

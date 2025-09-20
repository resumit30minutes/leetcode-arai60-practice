
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        kuriagari = 0
        l1_curr = l1
        l2_curr = l2
        while l1_curr is not None or l2_curr is not None:
            l1_val = l1_curr.val if l1_curr else 0
            l2_val = l2_curr.val if l2_curr else 0
            calc_result = l1_val + l2_val + kuriagari

            kuriagari = 0
            if calc_result >= 10:
                calc_result %= 10
                kuriagari = 1
            
            curr.next = ListNode(calc_result)
            curr = curr.next

            l1_curr = l1_curr.next if l1_curr else None
            l2_curr = l2_curr.next if l2_curr else None

        if kuriagari > 0:
            curr.next = ListNode(1)

        return dummy.next

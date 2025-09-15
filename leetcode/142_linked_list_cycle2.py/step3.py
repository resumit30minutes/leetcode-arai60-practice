class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        meeting_node = None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                meeting_node = slow
                break

        if meeting_node is None:
            return None
        
        result = head
        while meeting_node != result:
            meeting_node = meeting_node.next
            result = result.next

        return result
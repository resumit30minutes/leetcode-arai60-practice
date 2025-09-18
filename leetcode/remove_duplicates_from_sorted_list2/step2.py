class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last_unique_node = dummy
        current_node = head
        value_to_remove = None

        while current_node:
            if current_node.val == value_to_remove:
                current_node = current_node.next
                continue

            if current_node.next and current_node.val == current_node.next.val:
                value_to_remove = current_node.val
                continue

            last_unique_node.next = current_node
            last_unique_node = last_unique_node.next
            value_to_remove = None
            current_node = current_node.next

        last_unique_node.next = None
        return dummy.next

        
 


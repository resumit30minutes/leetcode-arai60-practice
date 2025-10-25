
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_set_node = set()
        curr = head
        while curr:
            if curr in visited_set_node:
                return curr

            visited_set_node.add(curr)
            curr = curr.next

        return None
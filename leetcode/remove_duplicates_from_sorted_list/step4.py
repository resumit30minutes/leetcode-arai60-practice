from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. 変数名の変更・改行削除・Noneのチェック方法を明示的に
        2. tail.next = Noneを常に行うように
        """
        checking = head
        dummy = ListNode()
        tail = dummy

        while checking is not None:
            if tail is not dummy and checking.val == tail.val:
                checking = checking.next
                continue

            tail.next = checking
            tail = checking
            checking = checking.next
            tail.next = None

        return dummy.next
    

    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ヘルパー関数がListNodeを取るように
        https://github.com/resumit30minutes/leetcode-arai60-practice/pull/4/files#r2497775701
        """
        return self._delete_duplicates(head, None)

    def _delete_duplicates(self, node: Optional[ListNode],  previous: Optional[ListNode]) -> Optional[ListNode]:
        if node is None:
            return None

        if previous is not None and node.val == previous.val:
            return self._delete_duplicates(node.next, previous)

        node.next = self._delete_duplicates(node.next, previous)
        return node


    def deleteDuplicates3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        帰りがけの再帰
        https://github.com/resumit30minutes/leetcode-arai60-practice/pull/4/files#r2497781908
        """
        if head is None:
            return None

        head.next = self.deleteDuplicates(head.next)
        if head.next is None or head.next.val != head.val:
            return head
        return head.next


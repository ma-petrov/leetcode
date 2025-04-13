# https://leetcode.com/problems/swap-nodes-in-pairs/


from __future__ import annotations


class ListNode:
    val: int
    next: ListNode | None


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        if not head or not head.next:
            return head

        previous = current = head
        head = head.next

        while current and current.next:
            previous.next = current.next

            temp = current.next
            current.next = current.next.next
            temp.next = current

            previous = current
            current = current.next
        
        return head

# https://leetcode.com/problems/merge-two-sorted-lists/


from __future__ import annotations


class ListNode:
    def __init__(self, val: int | None = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: ListNode | None,
        list2: ListNode | None,
    ) -> ListNode | None:

        # Чтобы не описывать начальный случай, в котором нужно выбрать вершину
        # из list1, list2 и присвоить в head, создана перменная head, которая
        # хранит несущесвующий узел. В ответе будет возвращен head.next.
        head = ListNode()
        current = head
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # После того, как один из списков закончился, в конец добавляется
        # остаток другого списка.
        current.next = list1 or list2

        return head.next

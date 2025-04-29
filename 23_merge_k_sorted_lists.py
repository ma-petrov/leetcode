# https://leetcode.com/problems/merge-k-sorted-lists/


from __future__ import annotations
import heapq


class ListNode:
    val: int
    next: ListNode | None


class HeapValue:
    def __init__(self, node: ListNode):
        self.value = node.val
        self.node = node
    
    def __lt__(self, other: HeapValue) -> bool:
        return self.value < other.value


class Solution:
    def mergeKLists(self, lists: list[ListNode] | None) -> ListNode | None:

        heap = [HeapValue(node) for node in lists if node]
        heapq.heapify(heap)
        current = new_list = ListNode()

        while heap:
            node = heapq.heappop(heap).node

            if node.next:
                heapq.heappush(heap, HeapValue(node.next))

            current.next = node
            current = current.next
        
        return new_list.next

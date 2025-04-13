# https://leetcode.com/problems/find-mode-in-binary-search-tree/


from __future__ import annotations
import collections


class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:

        level = collections.deque([root])
        count = collections.defaultdict(int)

        while level:            
            for _ in range(len(level)):
                if node := level.popleft():
                    count[node.val] += 1
                    level.append(node.left)
                    level.append(node.right)

        max_count = max(count.values())
        return [value for value, count in count.items() if count == max_count]

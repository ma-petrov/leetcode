# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


from __future__ import annotations
import collections


class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


class Solution:    
    def levelOrderBottom(
        self,
        root: TreeNode | None = None,
    ) -> list[list[int]]:

        order = []
        level: collections.deque[TreeNode] = collections.deque([root])

        while level:
            if values := [n.val for n in level if n]:
                order.append(values)

            for _ in range(len(level)):
                if node := level.popleft():
                    level.append(node.left)
                    level.append(node.right)

        return order[::-1]

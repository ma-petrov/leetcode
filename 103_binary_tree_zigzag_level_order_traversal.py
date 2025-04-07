# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


from __future__ import annotations
import collections


class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


class Solution:    
    def zigzagLevelOrder(
        self,
        root: TreeNode,
    ) -> list[list[int]]:
        if not root:
            return []

        is_odd = False
        order = []
        level: collections.deque[TreeNode] = collections.deque([root])

        while level:
            level_iterator = reversed(level) if is_odd else level
            order.append([n.val for n in level_iterator])

            for _ in range(len(level)):
                node = level.popleft()

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            is_odd = not is_odd

        return order

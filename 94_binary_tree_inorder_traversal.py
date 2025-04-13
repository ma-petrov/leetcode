# https://leetcode.com/problems/binary-tree-inorder-traversal/description/


from __future__ import annotations


class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


# ---- Решение 1 ----

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:

        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
            if root
            else []
        )


# ---- Решение 2 ----

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # Пока для текущей веришны есть левое поддерево, нужно обходить левое.
        # Как только левое поддерево пройдено, нужно вернуться в корень под-
        # дерева (stack.pop) и обходить правое (current = current.right).

        inorder, stack = [], []
        current: TreeNode | None = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            inorder.append(current.val)
            current = current.right

        return inorder

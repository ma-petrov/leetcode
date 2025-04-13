# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


from __future__ import annotations


class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


class Solution:
    def buildTree(
        self,
        inorder: list[int],
        postorder: list[int]
    ) -> TreeNode | None:

        if not inorder or not postorder:
            return None

        index = inorder.index(postorder[-1])

        return TreeNode(
            val=postorder[-1],
            left=self.buildTree(inorder[:index], postorder[:index]),
            right=self.buildTree(inorder[index + 1:], postorder[index:-1]),
        )

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


from __future__ import annotations


class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


class Solution:
    def buildTree(
        self,
        preorder: list[int],
        inorder: list[int],
    ) -> TreeNode | None:
        # preorder - массив вершин, получаемый обходом в дервеа глубину.
        # inorder - массив вершин дерева, где левое поддерево слева, правое 
        # поддерево - справа, вершина между подмассивами. Пусть есть дерево:
        #
        #     1
        #    / \
        #   2   5 
        #  / \
        # 3   4
        #
        # У которого preorder = [1, 2, 3, 4, 5], inorder = [3, 2, 4, 1, 5].
        # Левое поддерево в inorder - [3, 2, 4], правое - [5]. корень дерева
        # в inorder на позиции 3. В preorder (обход bfs) в начале всегда
        # вершина корня, затем идут вершины левого поддерева, затем - правого.
        # нельзя построить дерево только по preorder, так как неизвестно,
        # где граница между вершинами правого и левого поддеревьев. Так как
        # в inorder это граница - корень дерева, а значение корня известно по
        # preorder, то можно определить кол-во элементов левого и правого
        # поддеревьев в preorder.
        #
        # Пусть index == индекс корня (preorder[0]) в inorder, index == 3.
        # Тогда левое поддерево:
        # preorder[1:index + 1] == preorder[1:4] == [2, 3, 4]
        # inorder[:index] == inorder[:3] == [3, 2, 4]
        # Правое поддерево:
        # preorder[index + 1:] == preorder[4:] == [5]
        # inorder[index + 1:] == inorder[4:] == [5]

        if not preorder or not inorder:
            return None

        index = inorder.index(preorder[0])

        return TreeNode(
            val=preorder[0],
            left=self.buildTree(preorder[1:index + 1], inorder[:index]),
            right=self.buildTree(preorder[index + 1:], inorder[index + 1:]),
        )

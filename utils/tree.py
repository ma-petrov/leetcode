# Для отладки задач

from __future__ import annotations


class TreeNode:
    """Бинарное дерево."""

    def __init__(
        self,
        val: int | None = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
    
    @classmethod
    def from_list(cls, l: list[int]):
        """Создает бинарное дерево из списка последовательных уровней."""

        if not l:
            return None

        root = TreeNode(l[0])
        queue = [root]
        i = 1

        while i < len(l):
            node = queue.pop(0)

            if l[i] is not None:
                node.left = TreeNode(l[i])
                queue.append(node.left)

            i += 1

            if i < len(l) and l[i] is not None:
                node.right = TreeNode(l[i])
                queue.append(node.right)

            i += 1

        return root
    
    @property
    def tree_depth(self) -> int:
        """Возвращает глубину дерева."""

        if self.left is None and self.right is None:
            return 1

        left_depth = self.left.tree_depth if self.left else 0
        right_depth = self.right.tree_depth if self.right else 0

        return max(left_depth, right_depth) + 1
    
    @property
    def level_order(self) -> list[list[int]]:
        """Возвращает список уровней дерева."""

        level = [self]
        order: list[list[TreeNode]] = []

        while level:
            order.append(level)
            level = []
            
            for node in order[-1]:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

        return order
    
    def __repr__(self):
        return str(self.val)

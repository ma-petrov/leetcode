# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level


from __future__ import annotations
import collections


class TreeNode:
    val: int
    left: TreeNode | None
    right: TreeNode | None


class Solution:
    def minimumOperations(self, root: TreeNode | None = None) -> int:
        minimum_operations = 0

        for level in self.tree_levels(root):
            sorted_level = sorted(level)
            indexes = {value: index for index, value in enumerate(level)}

            for index in range(len(level)):
                value = level[index]

                # Значения на позициях в level должны совпадать со значениеми
                # в его отсортированной версии на тех же позициях. Если
                # значение не совпадает, то нужно поменять элемент с тем,
                # который должен стоять на этой позиции
                if value != sorted_level[index]:

                    # expected_value - значение, которое ожидается в index.
                    # i - индекс элемента, который должен быть на позции index.
                    expected_value = sorted_level[index]
                    i = indexes[expected_value]

                    level[index], level[i] = level[i], level[index]
                    indexes |= {expected_value: index, value: i}
                    minimum_operations += 1

        return minimum_operations

    def tree_levels(self, root: TreeNode | None = None) -> list[list[int]]:
        # Возвращает список уровней дерева, где каждый уровень представлен
        # в виде списка значений узлов уровня.

        tree_levels = []
        level = collections.deque([root])

        while level:
            if values := [node.val for node in level if node]:
                tree_levels.append(values)

            for _ in range(len(level)):
                if node := level.popleft():
                    level.append(node.left)
                    level.append(node.right)
            
        return tree_levels

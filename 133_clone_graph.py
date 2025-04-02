# ---- Вспомогательный код ----

from __future__ import annotations


class Node:
    def __init__(self, val: int | None = 0, neighbors: Node | None = None):
        self.val = val
        self.neighbors = neighbors or []


# ---- Решение ----

class Solution:
    def __init__(self):
        # Хранилище для созданных вершин. Служит для:
        # 1. Проверки, была ли уже вершина создана
        # 2. Хранит созданные вершины, чтобы заполнять список соседей.
        self.clonned_nodes = {}

    def cloneGraph(self, node: Node | None) -> Node | None:
        # Рекурсивно клонирует граф на основе алгоритма поиска в глубину.

        if node is None:
            return None
        
        # Если вершина уже была создана, для нее просто возвращается ссылка.
        # Ссылку нужно возвращать для заполнения соседей вершины, которая
        # ссылается на текущую вершину.
        if node.val in self.clonned_nodes:
            return self.clonned_nodes[node.val]
        
        # node.neighbors - список с ссылками, его нельзя передавать напрямую,
        # иначе в new_node.neighbors сохранятся ссылки на старые экземпляры
        # Node. Вместо этого далее рекурсивно вызывается функция cloneGraph
        # и возварщает новые экземпляры соседей текущей вершины.
        new_node = Node(val=node.val)
        self.clonned_nodes[new_node.val] = new_node
        
        # Клонирование соседей.
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        
        return new_node

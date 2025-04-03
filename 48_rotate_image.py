from __future__ import annotations


Offset = tuple[int, int]
Matrix = list[list[int]]


class Direction:
    left: Offset = (0, -1)
    right: Offset = (0, 1)
    up: Offset = (-1, 0)
    down: Offset = (1, 0)


class Matrix:
    def __init__(self, values: list[list[int]]):
        self.values = values
    
    def __getitem__(self, element: Element) -> int:
        return self.values[element.x][element.y]
    
    def __setitem__(self, element: Element, value: int):
        self.values[element.x][element.y] = value


class Element:
    # Координаты элемента матрицы

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, offset: Offset) -> Element:
        # Вычисление координат следующего элемента относительно текущего
        # элемента и смещения.

        return Element(self.x + offset[0], self.y + offset[1])


def rotate_square(m: Matrix, length: int, offset: int | None = 0):
    # Сдвигает по кругу элементы "квадрата" матрицы.

    # a, b, c, d - начальные точки сторон квадрата, левая верхняя, правая
    # верхняя, правая нижняя, левая нижняя
    a = Element(0 + offset, offset)
    b = Element(0 + offset, length - 1 - offset)
    c = Element(length - 1 - offset, length - 1 - offset)
    d = Element(length - 1 - offset, offset)
    
    for _ in range(length - offset * 2 - 1):
        # На каждом шаге текущие точки перезаписываются по кругу, а затем
        # сдвигаются в свои стороны
        
        m[a], m[b], m[c], m[d] = m[d], m[a], m[b], m[c]

        a += Direction.right
        b += Direction.down
        c += Direction.left
        d += Direction.up


class Solution:
    def rotate(self, matrix: list[list[int]]) -> list[list[int]]:
        # Сдвигает матрицу слоями, "квадратами". Всего "Квадратов", которые
        # нужно сдвинуть - length // 2

        matrix_object = Matrix(matrix)
        length = len(matrix)

        for offset in range(length // 2):
            rotate_square(m=matrix_object, length=length, offset=offset)

        return matrix_object.values

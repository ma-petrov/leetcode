from __future__ import annotations

import typing


Direction = tuple[int, int]
Matrix = list[list[int]]


class Element:
    # Хранит координаты элемента матрицы и может выполнять операции над 
    # значением в любой матрице, которая будет передана ему через параметры.

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, direction: Direction) -> Element:
        # Для чистоты кода операция вычисления следующего элемента выполняется
        # с помощью оператора сложения.

        return Element(self.x + direction[0], self.y + direction[1])
    
    def value(self, matrix: Matrix):
        return matrix[self.x][self.y]
    
    def invalid_or_none(self, matrix: Matrix) -> bool:
        # Проверяет, выходят ли координаты элемента за размер матрицы или
        # является ли значение элемента None.

        return not (
            0 <= self.x < len(matrix)
            and 0 <= self.y < len(matrix[0])
            and matrix[self.x][self.y] is not None
        )
    
    def set_none(self, matrix: Matrix):
        matrix[self.x][self.y] = None


def create_direction_iterator() -> typing.Generator[Direction, None, None]:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    current = 0

    while True:
        yield directions[current]
        current = (current + 1) % 4


def create_spiral_matrix_iterator(
    matrix: Matrix
) -> typing.Generator[int, None, None]:
    # Управляет обходом матрицы через операцию вычисления следующего элемента
    # относительно текущего элемента и направления, операцию смены направления.
    # При этом стратегия смены направления вынесена в отдельный объект. При
    # желании можно поменять направление обхода через direction_iterator.

    current = Element(0, 0)
    direction_iterator = create_direction_iterator()
    direction = next(direction_iterator)

    while True:
        yield current.value(matrix)
        next_element = current + direction

        # Если следующий элемент невалидный (выходит за границы матрицы,
        # или уже был пройден итератором), тогда меняется направление и
        # заново вычисляется следующий элмент.
        if next_element.invalid_or_none(matrix):
            direction = next(direction_iterator)
            next_element = current + direction

            # Если после смены напрвления элемент опять невалидный, значит
            # больше нельзя получить новый элемент из матрицы.
            if next_element.invalid_or_none(matrix):
                break

        # текущий элемент помечается как пройденный (None)
        current.set_none(matrix)
        current = next_element


class Solution:
    def spiralOrder(self, matrix: Matrix) -> list[int]:
        return list(create_spiral_matrix_iterator(matrix))

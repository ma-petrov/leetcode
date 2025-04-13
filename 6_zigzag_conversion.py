# https://leetcode.com/problems/zigzag-conversion/


import typing


def create_row_num_iterator(
    num_rows: int,
) -> typing.Generator[int, None, None]:
    # Возвращает номер строки, в которой должна находиться буква, в зависимости
    # кол-ва строк.

    position, direction = 0, 1
    num_rows -= 1
    
    while True:
        for _ in range(num_rows):
            yield position
            position += direction
        
        direction = -direction


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        row_num_iterator = create_row_num_iterator(num_rows)
        rows = [[] for _ in range(num_rows)]

        for letter in s:
            rows[next(row_num_iterator)].append(letter)

        return "".join("".join(row) for row in rows)

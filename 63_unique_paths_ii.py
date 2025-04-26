# https://leetcode.com/problems/unique-paths-ii/description/


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: list[list[int]]) -> int:

        # Каждый элемент хранит кол-во путей, которыми робот может "дойти" до
        # соотвутсвующей клетки карты.
        count = [
            [0] * (len(obstacle_grid[0]) + 1)
            for _ in range(len(obstacle_grid) + 1)
        ]

        # Имитация того, что робот "пришел" в верхнюю левую клетку карты
        # "сверху", чтобы не добавлять граничное условие в основную логику.
        count[0][1] = 1

        for x in range(len(obstacle_grid)):
            for y in range(len(obstacle_grid[0])):
                if obstacle_grid[x][y] == 0:
                    count[x + 1][y + 1] = count[x][y + 1] + count[x + 1][y]

        return count[-1][-1]

# https://leetcode.com/problems/trapping-rain-water-ii/


import heapq, typing


def border_iterator(
    xsize: int,
    ysize: int,
) -> typing.Generator[tuple[int, int], None, None]:
    # Возвращает итератор по координатам элементов матрицы на границе
    # по часовой стрелке начиная с левого верхнего угла.

    current = 0, 0

    for offset in (
        *[(0, 1)] * (ysize - 1),
        *[(1, 0)] * (xsize - 1),
        *[(0, -1)] * (ysize - 1),
        *[(-1, 0)] * (xsize - 1),
    ):
        yield current
        current = current[0] + offset[0], current[1] + offset[1]


class Solution:
    def trapRainWater(self, height_map: list[list[int]]) -> int:

        xsize, ysize = len(height_map), len(height_map[0])
        water, max_height, heap, visited = 0, 0, [], set()

        # Добавление элементов, расположенных на краю карты.
        for x, y in border_iterator(xsize=xsize, ysize=ysize):
            heapq.heappush(heap, (height_map[x][y], x, y))
            visited.add((x, y))

        # Пока в куче есть элементы, выполняются попытки найти соседний
        # элемент, каторый можно "заполнить" водой.
        while heap:

            # Из кучи всегда берется минимальный элемент. Так как изначально
            # в куче лежат все "столбики" на границе, то минимальный возможный
            # уровень воды в любой клетке внутри точно не ниже уровня самого
            # маленького "столбика" на краю карты, даже если в середине
            # карты "столбики" ниже. Так как из кучи всегда берется клетка
            # с самым маленьким уровнем, то сначала водой будут "заполнятся"
            # нижние участки, и никогда не получится, что столбик будет
            # "заполнен" водой выше уровнем, чем "берега", которые ограничивают
            # "лужу", в которой этот столбик находится.
            height, x, y = heapq.heappop(heap)
            max_height = max(max_height, height)

            # Для каждого соседнего "столбика" выполняется попытка "заполнить"
            # его водой до уровня max_height и добавить его в кучу.
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):

                nx, ny = x + dx, y + dy
                
                # Если соседний элемент уже был посещен, или соседний элемент
                # не существует (координаты выходят за границы карты), то он
                # пропускается
                if (
                    (nx, ny) in visited
                    or not (0 <= nx < xsize and 0 <= ny < ysize)
                ):
                    continue

                # Если столбик nx, ny по высоте меньше, чем уровнь max_height,
                # то он "заполнится водой". В противном случае функция max
                # заменяет отрицательное значение на 0.
                water += max(0, max_height - height_map[nx][ny])
                heapq.heappush(heap, (height_map[nx][ny], nx, ny))
                visited.add((nx, ny))

        return water

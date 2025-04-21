# https://leetcode.com/problems/count-the-hidden-sequences/description/


class Solution:
    def numberOfArrays(
        self,
        differences: list[int],
        lower: int,
        upper: int
    ) -> int:
        # Диапазон значений массива - разница между максимальным и минимальным
        # элементом xmax - xmin.
        # Пусть есть x0, тогда (xmax - x0) + (xmin - x0) == xmax - xmin.
        # То есть, зная разницу между xmax и x0; xmin и x0, можно найти разницу
        # между xmax и xmin, при этом от x0 значение не зависит. Поэтому за x0
        # можно взять нулевое значение и далее считать накопленную разницу
        # (current) относительно x0.

        current, min_difference, max_difference = 0, 0, 0

        for difference in differences:

            current += difference
            min_difference = min(min_difference, current)
            max_difference = max(max_difference, current)
        
        return max((upper - lower) - (max_difference - min_difference) + 1, 0)

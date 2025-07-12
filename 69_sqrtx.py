# https://leetcode.com/problems/sqrtx/


import typing


T = typing.TypeVar("Comparable")


class Solution:
    def mySqrt(self, x: int) -> int:
        return self.range_binary_search(target=x, range_min=0, range_max=x, key=lambda t: t ** 2)
    
    def range_binary_search(
        self,
        target: T,
        range_min: T,
        range_max: T,
        key: typing.Callable[[T], T] | None = None,
        mid: typing.Callable[[T, T], T] | None = None,
    ) -> T | None:
        key = key or (lambda t: t)
        mid = mid or (lambda range_min, range_max: (range_max + range_min) // 2)

        while range_min <= range_max:
            mid_value = mid(range_min, range_max)

            if key(mid_value) == target:
                return mid_value

            if key(mid_value) > target:
                range_max = mid_value - 1
            else:
                range_min = mid_value + 1
        
        # Так как поиск примерный, у округлять нужно до нижней границы, то возвращается range_max,
        # если не было найдено точное совпадение.
        return range_max

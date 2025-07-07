# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/


import collections


class FindSumPairs:

    def __init__(self, a: list[int], b: list[int]):
        self.a_counter = collections.Counter(a)
        self.b_counter = collections.Counter(b)
        self.b = b

    def add(self, index: int, value: int) -> None:
        self.b_counter[self.b[index]] -= 1
        self.b[index] += value
        self.b_counter[self.b[index]] += 1

    def count(self, target: int) -> int:
        return sum(
            a_count * self.b_counter[target - a_value]
            for a_value, a_count in self.a_counter.items()
        )

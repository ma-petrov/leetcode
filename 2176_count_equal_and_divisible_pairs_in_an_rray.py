# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/


import collections


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:

        self.k = k

        groups = collections.defaultdict(list)
        for index, num in enumerate(nums):
            groups[num].append((index, num))

        return sum(map(self.count_paires_in_group, groups.values()))

    def count_paires_in_group(self, elements: list[tuple[int, int]]) -> int:

        return sum(
            1
            if (
                elements[i][1] == elements[j][1]
                and (elements[i][0] * elements[j][0]) % self.k == 0
            )
            else 0
            for i in range(len(elements) - 1)
            for j in range(i + 1, len(elements))
        )

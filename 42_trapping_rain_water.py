# https://leetcode.com/problems/trapping-rain-water/


import itertools


class Solution:
    def trap(self, height: list[int]) -> int:

        lmax = itertools.accumulate(height, max)
        rmax = list(itertools.accumulate(height[::-1], max))[::-1]

        return sum(
            max(0, min(lm, rm) - h)
            for h, lm, rm in zip(height, lmax, rmax)
        )

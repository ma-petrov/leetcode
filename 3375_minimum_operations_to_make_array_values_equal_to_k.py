# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        min_num = min(nums)

        if k > min_num:
            return - 1

        unique_count = len(set(nums))
        return unique_count - 1 if k == min_num else unique_count

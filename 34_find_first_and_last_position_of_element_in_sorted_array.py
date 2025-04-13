# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:        
        for i in range(len(nums)):
            if nums[i] == target:
                for j in range(i + 1, len(nums)):
                    if nums[j] != target:
                        return [i, j - 1]
                return [i, len(nums) - 1]
        return [-1, -1]

# https://leetcode.com/problems/maximum-erasure-value/


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        # См. задачу #3

        sub_array = set()
        max_sum, current_sum, left = 0, 0, 0

        for num in nums:

            while num in sub_array:
                current_sum -= nums[left]
                sub_array.remove(nums[left])
                left += 1

            current_sum += num
            sub_array.add(num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

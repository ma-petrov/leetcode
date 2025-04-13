# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        nums.sort()
        min_difference = float("inf")
        closest_sum = None
        
        for left in range(len(nums) - 2):
            middle, right = left + 1, len(nums) - 1

            while middle < right:
                current_sum = nums[left] + nums[middle] + nums[right]
                difference = abs(current_sum - target)

                if difference < min_difference:
                    min_difference = difference
                    closest_sum = current_sum

                if current_sum > target:
                    right -= 1
                else:
                    middle += 1

        return closest_sum

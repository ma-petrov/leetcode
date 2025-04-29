# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:

        max_num = max(nums)
        subarrays_count = max_num_count = right = 0

        for left in range(len(nums)):

            while right < len(nums) and max_num_count < k:
                if nums[right] == max_num:
                    max_num_count += 1
                right += 1
            
            if max_num_count < k:
                break
            
            subarrays_count += len(nums) - right + 1
            
            if nums[left] == max_num:
                max_num_count -= 1
        
        return subarrays_count

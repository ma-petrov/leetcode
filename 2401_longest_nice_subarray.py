# https://leetcode.com/problems/longest-nice-subarray/


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        max_length, left = 0, 0

        for right, num in enumerate(nums):

            # Для нового элемента нужно проверить операцию & с каждым
            # элементом текущего подмассива. Новая левая граница будет
            # после элемента с наибольшим индексом, котороый НЕ удовлетворяет
            # условию.
            for index in range(left, right):
                if num & nums[index] != 0:
                    left = index + 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

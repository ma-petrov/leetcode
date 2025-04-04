# https://leetcode.com/problems/longest-nice-subarray/


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:

        # Текущий подмасив, которой гарантировано удовлетворяет условию.
        # (операция & над всеми парами элементов возвращает 0)
        subarray = set()
        max_length, left = 0, 0

        for right, num in enumerate(nums):
            old_left = left

            # Для нового элемента нужно проверить операцию & с каждым
            # элементом текущего подмассива. Новая левая граница будет
            # после элемента с наибольшим индексом, котороый НЕ возвращает
            # ноль при побитовом сложении с текущим элементом.
            for index in range(left, right):
                if num & nums[index] != 0:
                    left = index + 1
            
            max_length = max(max_length, right - left + 1)
            subarray -= set(nums[old_left:left])
            subarray.add(num)
        
        return max_length

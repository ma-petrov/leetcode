# https://leetcode.com/problems/longest-nice-subarray/


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        # Границы текущего подмасива - left, right. Все пары элементов
        # гарантировано удовлетворяет условию (операция & возвращает 0),
        # так как каждый новый элемент добавляется после того, как из
        # подмассива будут удалены все элементы, не удовлетворяющие условию
        # в паре с новым элементом.

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

# https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Алгоритм быстрой выборки на основе алгоритма быстрой сортировки
        
        middle = nums[0]
        left = [n for n in nums if n > middle]
        right = [n for n in nums if n < middle]
        equal = [n for n in nums if n == middle]

        # Если длина массива left (значения больше middle) > k, тогда искомое
        # значение находится в k.
        if len(left) >= k:
            return self.findKthLargest(left, k)

        # Если длина left меньше k, но длина left + middle - больше k, тогда
        # искомое значение находится среди значений middle, а значит ответ
        # найден.
        if len(left) + len(equal) >= k:
            return middle

        # В остальных случаях - искомое значение находится в right (значения
        # меньше middle). Но так как среди наибольших значений сначала будут
        # идти значения из left и middle, а потом уже из right. Тогда если в
        # глобальном массиве искомый элемент - k-ый, то в right он будет
        # на месте k - len(left) - len(equal).
        return self.findKthLargest(right, k - len(left) - len(equal))

# https://leetcode.com/problems/count-complete-subarrays-in-an-array/


import collections


class Solution:

    def countCompleteSubarrays(self, nums: list[int]) -> int:

        right, complete_subarrays_count, unique_count = 0, 0, len(set(nums))
        subarray_elements = collections.defaultdict(int)

        # Для каждого i-го элемента left
        for left in range(len(nums)):

            # нужно найти такой минимальный элемент right, так что на отрезке
            # left:right есть все элементы из массива.
            while right < len(nums) and len(subarray_elements) < unique_count:
                subarray_elements[nums[right]] += 1
                right += 1
            
            # Если кол-во уникальных элементов в подмассиве меньше, чем в
            # массиве, значит right дошел до границы масссива, и тогда больше
            # нет подмассивов, удовлетворяющих условию.
            if len(subarray_elements) < unique_count:
                break

            # Иначе кол-во подмассивов для left, удовлетворяющих условию, равно
            # кол-ву элементов len(nums) - right + 1 (right включая), так как
            # для i-го left все подмассивы left:j, где j >= right удовлетворяют
            # условию.
            complete_subarrays_count += len(nums) - right + 1

            # Вычетание текущего nums[left] из подсчета кол-ва элементов в
            # подмассиве.
            subarray_elements[nums[left]] -= 1
            if subarray_elements[nums[left]] == 0:
                del subarray_elements[nums[left]]

        return complete_subarrays_count

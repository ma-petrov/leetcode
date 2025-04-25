# https://leetcode.com/problems/count-of-interesting-subarrays/


import collections, itertools


class Solution:
    def countInterestingSubarrays(
        self,
        nums: list[int],
        modulo: int,
        k: int,
    ) -> int:

        # Префиксная сумма кол-ва элментов, которые удовлетворяют условию.
        correct_modulo_prefix_sums = itertools.accumulate(
            [1 if num % modulo == k else 0 for num in nums]
        )

        # Кол-во (value) префиксных сумм (key), которые встретились в массиве
        # по модулю.
        preifx_sum_frequency = collections.defaultdict(int)
        preifx_sum_frequency[0] = 1
        subarrays_count = 0

        for prefix_sum in correct_modulo_prefix_sums:
            subarrays_count += preifx_sum_frequency[(prefix_sum - k) % modulo]
            preifx_sum_frequency[prefix_sum % modulo] += 1

        return subarrays_count

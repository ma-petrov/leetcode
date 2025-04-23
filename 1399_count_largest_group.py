# https://leetcode.com/problems/count-largest-group/description/


import collections


# ---- Решение 1 ----

class Solution:
    def countLargestGroup(self, n: int) -> int:

        groups_length = collections.defaultdict(int)
        max_length = 0

        for number in range(1, n + 1):
            key = self.digits_sum(number)
            groups_length[key] += 1
            max_length = max(max_length, groups_length[key])

        return sum(
            1
            for length in groups_length.values()
            if length == max_length
        )

    def digits_sum(self, number: int) -> int:
        # Сумма цифр в числе

        digits_sum = 0

        while number > 0:
            digits_sum += number % 10
            number //= 10
        
        return digits_sum


# ---- Решение 2 ----

class Solution:
    def countLargestGroup(self, n: int) -> int:

        digits_sums = map(self.digits_sum, range(1, n + 1))
        counts = collections.Counter(digits_sums).values()
        max_count = max(counts)
        return sum(1 for c in counts if c == max_count)

    def digits_sum(self, number: int) -> int:
        # Сумма цифр в числе

        return sum(map(int, str(number)))

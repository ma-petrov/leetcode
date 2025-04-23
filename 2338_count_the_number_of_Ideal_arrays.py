# https://leetcode.com/problems/count-the-number-of-ideal-arrays/


import functools


class Solution:
    modulo = 10 ** 9 + 7

    @functools.lru_cache(maxsize=None)
    def dfs(self, value: int, length: int):

        if length == self.n:
            return self.combinations[length - 1]

        result = self.combinations[length - 1]

        # divisible - число, которое делится на value в диапазоне
        # value <= divisible <= max_value
        for divisible in range(2 * value, self.max_value + 1, value):

            result += self.dfs(value=divisible, length=length + 1)
            result %= self.modulo

        return result

    def idealArrays(self, n: int, max_value: int) -> int:

        # Вместо двумерного массива для расчета C(n, k) используется одномерный
        # для экономии памяти, поэтому ниже в цикле происходит сложение не
        # C[i][j] = C[i - 1][j] + C[i - 1][j - 1], вместо этого массив
        # перезаписывается: C[j] += C[j - 1]
        self.combinations = [1] + [0] * 15
        self.max_value = max_value
        self.n = n

        for i in range(1, n):

            # Чтобы на каждом шаге брались старые значения (строка i - 1),
            # нужно обходить и перезаписывать массив combinations с конца.
            for j in range(min(15, i), 0, -1):

                # C(n, k) = C(n-1, k) + C(n-1, k-1)
                self.combinations[j] += self.combinations[j - 1]
                self.combinations[j] %= self.modulo

        combinations_count = 0

        for value in range(1, max_value + 1):
            combinations_count += self.dfs(value=value, length=1)
            combinations_count %= self.modulo

        return combinations_count

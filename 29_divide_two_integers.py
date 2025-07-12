# https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MAX = (1 << 31) - 1
        INT_MIN = - (1 << 31)

        is_negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while dividend >= divisor:
            # На каждой итерации вычисляется максимальное count,
            # такое что остаток dividend >= divisor * (2 ** count)

            count = 0
            while dividend >= (divisor << (count + 1)):
                count += 1

            result += 1 << count
            dividend -= divisor << count

        return max(INT_MIN, -result) if is_negative else min(INT_MAX, result)

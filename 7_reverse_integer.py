# https://leetcode.com/problems/reverse-integer/


# ---- Решение 1 ----

class Solution:
    max_value = 2 ** 31 - 1
    min_value = -(max_value) - 1

    def reverse(self, x: int) -> int:

        digits, multiplier = [], 1

        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        while x > 0:
            digits.append(x % 10)
            x //= 10

        for digit in reversed(digits):
            x += digit * multiplier
            multiplier *= 10
        
        x = sign * x
        if x > self.max_value or x < self.min_value:
            return 0
        return x


Solution().reverse(-123)


# ---- Решение 2 ----

class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)
        x = "-" + x[:0:-1] if x.startswith("-") else x[::-1]
        x = int(x)
        
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        
        return x

# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        for i in range(len(s) - 1):
            sign = -1 if numbers[s[i]] < numbers[s[i + 1]] else 1
            total += numbers[s[i]] * sign
        return total + numbers[s[-1]]

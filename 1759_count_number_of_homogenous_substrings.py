# https://leetcode.com/problems/count-number-of-homogenous-substrings/


class Solution:
    modulo = 10 ** 9 + 7

    def countHomogenous(self, s: str) -> int:

        s += " "
        left, total_count = 0, 0

        for right in range(1, len(s)):
            if s[left] != s[right]:
                n = right - left
                total_count += n * (n + 1) // 2 % self.modulo
                left = right
        
        return total_count % self.modulo

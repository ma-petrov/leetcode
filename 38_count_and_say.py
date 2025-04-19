# https://leetcode.com/problems/count-and-say/


import itertools


# ---- Решение 1 ----

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"
        
        return self.rle(self.countAndSay(n - 1))
    
    def rle(self, s: str) -> str:
        
        s += " "
        left, compressed = 0, ""
        for right in range(1, len(s)):
            if s[left] != s[right]:
                compressed += str(right - left) + s[left]
                left = right
        return compressed


# ---- Решение 2 ----

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        return self.rle(self.countAndSay(n - 1))
    
    def rle(self, s: str) -> str:

        return "".join(
            f"{len(list(group))}{digit}"
            for digit, group in itertools.groupby(s)
        )

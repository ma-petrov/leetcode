# https://leetcode.com/problems/minimum-window-substring/


import collections


class Frequency:
    def __init__(self, string: str):
        self.not_presented = set(string)
        self.required_frequency = collections.Counter(string)
        self.frequency = {letter: 0 for letter in string}
    
    @property
    def is_all_presendted(self) -> bool:
        return not self.not_presented

    def add(self, letter: str):
        if letter in self.required_frequency:
            self.frequency[letter] += 1
            if self.frequency[letter] >= self.required_frequency[letter]:
                self.not_presented.discard(letter)
    
    def sub(self, letter: str):
        if letter in self.required_frequency and self.frequency[letter] > 0:
            self.frequency[letter] -= 1
            if self.frequency[letter] < self.required_frequency[letter]:
                self.not_presented.add(letter)


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        frequency = Frequency(t)
        right, min_length, window = 0, len(s), ""

        for left in range(len(s)):

            while right < len(s) and not frequency.is_all_presendted:
                frequency.add(s[right])
                right += 1

            if not frequency.is_all_presendted:
                break

            if (length := right - left) <= min_length:
                min_length = length
                window = s[left:right]
            
            frequency.sub(s[left])

        return window

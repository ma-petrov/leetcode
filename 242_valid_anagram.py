import collections


# ---- Вариант 1 ----

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


# ---- Вариант 2 ----

class Solution:
    offset = ord("a")

    def isAnagram(self, s: str, t: str) -> bool:
        return self.word_to_vector(s) == self.word_to_vector(t)
    
    def word_to_vector(self, word: str) -> list[int]:
        vector = [0] * 26
        for letter in word:
            vector[ord(letter) - self.offset] += 1
        return vector

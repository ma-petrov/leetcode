# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/


class Solution:
    offset = ord("a")

    def removeAnagrams(self, words: list[str]) -> list[str]:
        result = []
        last_vector = None

        for word in words:           
            if (vector := self.word_to_vector(word)) != last_vector:
                last_vector = vector
                result.append(word)
        
        return result

    def word_to_vector(self, word: str) -> list[int]:
        # Почему-то в этой задаче заботает быстрее, чем collections.Counter,
        # но в 242 collections.Counter быстрее.

        vector = [0] * 26
        for letter in word:
            vector[ord(letter) - self.offset] += 1
        return vector

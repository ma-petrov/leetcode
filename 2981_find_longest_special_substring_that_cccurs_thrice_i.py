# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/


import collections


class Solution:
    def maximumLength(self, s: str) -> int:
        
        # Хранит кол-во подстрок длины length, length - 1, length - 2.
        substrings = collections.defaultdict(int)

        length = 1
        for index, letter in enumerate(s):

            # Увеличение счетчиков длин подстрок.
            substrings[(letter, length)] += 1
            if length - 1 > 0:
                substrings[(letter, length - 1)] += 1
            if length - 2 > 0:
                substrings[(letter, length - 2)] += 1

            # Если следующая буква отличается, для слудующего шага length
            # сбрасывается, иначе length увеличивается на 1.
            if index < len(s) - 1 and letter != s[index + 1]:
                length = 1
            else:
                length += 1
        
        # Поиск максимальной длины подстроки среди тех подстрок, которые
        # встретились больше 3 раз.
        max_length = -1
        for (_, length), count in substrings.items():
            if count >= 3:
                max_length = max(max_length, length)
        return max_length

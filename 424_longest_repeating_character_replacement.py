# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Подстрока должна быть непрерывной, поэтому для перебора всех
        # вариантов достаточно скользящего окна. Наибольшая подстрока
        # получится, если заменять символы на те, которых больше всего в
        # подстроке. Кол-во символов в подстроке хранится в словаре letters
        # Левую границу нужно двигать тогда, когда кол-во заменяемых букв
        # (rigth - left + 1 - most_frequent_count) превышает k.

        letters = {}
        max_length, left = 0, 0

        for right, letter in enumerate(s):

            # Обновление кол-ва символов в подстроке и кол-во буквы, которая
            # встречается чаще всего в подстроке. 
            letters[letter] = letters.get(letter, 0) + 1

            # Если кол-во заменяемых букв превышает k, нужно даигать левую
            # границу.
            while right - left + 1 - max(letters.values()) > k:
                letters[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

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
        max_length, left, most_frequent_count = 0, 0, 0

        for right in range(len(s)):
            letter = s[right]

            # Обновление кол-ва символов в подстроке и кол-во буквы, которая
            # встречается чаще всего в подстроке. 
            letters[letter] = letters.get(letter, 0) + 1
            most_frequent_count = max(most_frequent_count, letters[letter])

            # Если кол-во заменяемых букв превышает k, нужно даигать левую
            # границу. Внутри while не обновляется most_frequent_count, так как
            # в этом нет необходимости, для расчета max_length переменная
            # most_frequent_count не нужно. most_frequent_count обновится в
            # начале следующей итерация цикла for.
            while right - left + 1 - most_frequent_count > k:
                letters[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

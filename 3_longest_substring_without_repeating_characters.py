# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Так как подстрока должна быть непрерывной, то задача сводится к 
        # итерации окном по строке с запоминанием максимального значения
        # длины подстроки без повторяющихся символов.

        # Множество букв, которые принадлежат текущей подстроке.
        substring_letters = set()

        # Максимальная длина подстроки, левый указатель окна.
        max_length, left = 0, 0

        # left - указатель на первый символ подстроки, letter - текущий символ
        for letter in s:

            # Сдвиг левого указателя, когда правый дошел до такой буквы, с 
            # которой подстрока уже не уникальна. Проверять на максимальное
            # значение смысла нет, так как длина только уменьшается.
            while letter in substring_letters:
                substring_letters.remove(s[left])
                left += 1

            # Сдвиг правого указателя, пока буквы в подстроке уникальны. С
            # каждым сдвигом вычисляется новое значение max_length, так как
            # подстрока увеличивается.
            substring_letters.add(letter)
            max_length = max(max_length, len(substring_letters))

        return max_length

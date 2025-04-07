# https://leetcode.com/problems/longest-palindromic-substring/


import typing


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Середины всех палиндромов в строке:
        # 1. Для палиндромов нёчетной длины - каждый элемент строки.
        # 2. Для чётной - пары (0, 1), (1, 2), ..., (n - 1, n)
        # Задача сводится к перебору для всех середин максимального палиндрома
        # и поиск среди них глобального.

        length = len(s)

        # Границы палиндрома максимальной длины.
        max_palindrome = 0, 1

        for left, right in self.palindromes_middle(length):
            # left, right - левая и правая границы, на каждом шаге начльные
            # значения - середина палиндромной строки.

            # Движение от середины к краям, пока совпадают символы (подстрока
            # является палиндромом)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Когда найдены неодинаковые пары символов, или достигнута граница
            # строки - для дайнной середины найден палиндром максимальной
            # длины. Нужно сравнить его с длиной глобального.
            if right - left - 1 > max_palindrome[1] - max_palindrome[0]:
                max_palindrome = left + 1, right

        return s[max_palindrome[0]:max_palindrome[1]]

    def palindromes_middle(
        self,
        length: int,
    ) -> typing.Generator[tuple[int, int], None, None]:
        # Возвращает список из кортежей в формате:
        # [(0, 0), (0, 1), (1, 1), (1, 2), ..., (length - 1, length - 1)]

        # Альтернативный метод в 1 строку, но занимает в памяти место:
        # return [(i, i + k) for i in range(length) for k in range(2)][:-1]

        for i in range(length - 1):
            for k in range(2):
                yield i, i + k
        yield length - 1, length - 1

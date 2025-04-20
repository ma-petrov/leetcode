# https://leetcode.com/problems/rabbits-in-forest/


import collections, math


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        # Кролики, которые имеют одинаковый цвет, принадлежат к одной группе,
        # поэтому будут называть одинаковое число. Если m кроликов назвали
        # число n, то в одной группе не может быть больше чем n + 1 кроликов,
        # если m > n, то групп больше чем 1. Минимальное кол-во групп для
        # m кроликов и числа n - округеленное вверх значение m / n. Тогда
        # кол-во кроликов во всех группах - (n + 1) * ceil(m / n), где n + 1
        # - кол-во кроликов в группе.

        answers_count = collections.Counter(answers)
        return sum(map(self._num_rabbits, answers_count.items()))
    
    def _num_rabbits(self, answers_count_item: tuple[int, int]) -> int:
        # Реализация вышеописанной формулы, m - count, n - answers

        answers, count = answers_count_item
        return (answers + 1) * math.ceil(count / (answers + 1))

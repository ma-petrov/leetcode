# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


import collections
import math


class Solution:
    def minDeletions(self, string: str) -> int:
        # Частоты сортируются в порядке невозрастания. Если f[i] == f[i-1],
        # то f[i-1] приравнивается к f[i-1] - 1. Если частота f[i] > f[i-1], то
        # значит существует частота f[i-n] (n > 0), такая что f[i] == f[i-n], 
        # так как если бы такая частота изначально не встречалась, то f[i] не
        # могла бы располагаться на i-ом месте, из-за того, что массив
        # изначально отсортирован в порядке невозрастания. Аналогично для
        # каждого значения в промежутке [f[i-1]: f[i]], следовательно все
        # частоты в этом промежутке уже встречались. Тогда частота f[i] должна
        # быть приравнена к f[i-1] - 1. Из этого следуюет частный случай, когда
        # f[i-1] == 0, в таком случае f[i] приравнивается тоже к 0 (а не к -1).
        # Если f[i] < f[i-1], то f[i] еще не встречалась, так как любое f[i-n]
        # (n > 0) не может быть меньше f[i].

        frequency_counter = collections.Counter(string)
        deletions = 0
        previous_frequency = math.inf

        for frequency in sorted(frequency_counter.values(), reverse=True):

            if previous_frequency == 0:
                deletions += frequency

            elif frequency >= previous_frequency:
                deletions += frequency - (previous_frequency - 1)
                previous_frequency -= 1

            else:
                previous_frequency = frequency

        return deletions

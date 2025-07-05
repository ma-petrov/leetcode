# https://leetcode.com/problems/query-kth-smallest-trimmed-number/


class Solution:
    def smallestTrimmedNumbers(self, numbers: list[str], queries: list[list[int]]) -> list[int]:
        self._length = len(numbers)
        self._numbers = numbers
        self._trimmed_sorted_numbers = {}
        return [self._kth_smallest(k=k, trim=trim) for k, trim in queries]

    def _kth_smallest(self, k: int, trim: int) -> int:
        """Возвращает индекс k-ого наименьшего числа после триммирования.
        
        Хранит в переменной `self._trimmed_sorted_numbers` список индексов триммированного массива, отсортированный по
        значинию (сортировка выполняется после тримиирования). Если для trim еще не вычислялся такой список, то сначала
        вычисляет его, затем возвращает значение k-ого индекса ключу trim из `self._trimmed_sorted_numbers`.
        """

        if trim not in self._trimmed_sorted_numbers:
            trimmed = [int(number[-trim:]) for number in self._numbers]
            self._trimmed_sorted_numbers[trim] = sorted(range(self._length), key=lambda index: trimmed[index])

        return self._trimmed_sorted_numbers[trim][k - 1]

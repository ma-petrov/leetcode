# https://leetcode.com/problems/count-good-triplets-in-an-array/


class BinaryIndexedTree:
    # Дерево Фенвика
    # https://www.youtube.com/watch?v=uSFzHCZ4E-8

    def __init__(self, size: int):
        self.size = size
        self.array = [0] * (size + 1)

    def lowbit(self, x) -> int:
        # Инвертирует самый младший установленный бит, например 0110 -> 0100.
        # 
        # Отрицательное число хранится, как ~x + 1 (побитовое НЕ, инверсия,
        # плюс 1). Если применить операцию & (побитовое И) к числу и его
        # побитовой инверсии, то результат будет 0. Но если предварительно
        # к инвертированному числу прибавить 1, то произойдет следующее:
        # пусть x == 40 == 0b101000, инвертированное число - 0b010111,
        # младший установленный бит x находится в 4 разряде, в инвертированной
        # версии соответственно, это 0, а биты справа - единицы. Прибавление
        # к ним 1 даст 0b011000, и тогда при операции & получим 0b001000,
        # т.е. младший установленный бит числа x.

        return x & -x

    def update(self, index: int, difference: int):
        # Обвновление суммы тех интервалов, которые перекрывают index.

        while index <= self.size:
            self.array[index] += difference
            index += self.lowbit(index)

    def query(self, index: int) -> int:
        # Сложение всех интервалов, которые составляют сумму от 0 до index.

        sum_value = 0
        while index > 0:
            sum_value += self.array[index]
            index -= self.lowbit(index)
        return sum_value


class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:

        positions = {num: index for index, num in enumerate(nums2, start=1)}
        good_triplets_count = 0
        length = len(nums1)
        tree = BinaryIndexedTree(length)

        for num in nums1:
            position = positions[num]

            # Кол-во элементов слева умножить на кол-во элементов справа минус
            # кол-во элементов, которая встретилось слева.
            good_triplets_count += (
                tree.query(position) * (
                    length
                    - position
                    - tree.query(length)
                    + tree.query(position)
                )
            )

            # Увеличение кол-во встретившихся элементов из nums1 для слева от
            # позиции position в nums2
            tree.update(position, 1)

        return good_triplets_count



nums1 = [2, 0, 1, 3]
nums2 = [0, 1, 2, 3]
print(Solution().goodTriplets(nums1, nums2))

# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/


class Solution:
    modulo = 10 ** 9 + 7

    def numSubseq(self, numbers: list[int], target: int) -> int:

        # В отсортированном массиве для любого его подмассива справедливо
        # утверждение, что самый левый элемент - максимальный, а самый правый
        # элемент - минимальный.
        numbers.sort()
        numbers_length = len(numbers)
        right, subsequences_count = len(numbers) - 1, 0

        # Таблица степеней двоек.
        powers_of_two = [1] * numbers_length
        for i in range(1, numbers_length):
            powers_of_two[i] = (powers_of_two[i-1] * 2) % self.modulo

        # Для каждого левого элемента выполняется поиск правого так, что сумма
        # левого и правого <= целевому значению.
        for left, left_number in enumerate(numbers):

            # Поиск правого элемента.
            while right >= left and left_number + numbers[right] > target:
                right -= 1
            
            if left > right:
                break
            
            # Если сумма левого и правого элементов <= target, значит все
            # подпоследовательности, где любой из элементов от левого до
            # правого, подходят. Количество таких подпоследовательностей равно 
            # 2 ** (right - left) - каждый элемент между left и right может
            # быть либо включён, либо нет.
            subsequences_count += powers_of_two[right - left]
            subsequences_count %= self.modulo

        return subsequences_count

# ---- Вариант 1 ----

class Solution:
    def reverseBits(self, n: int) -> int:

        # Преобразвание числа в бинарное представление
        binary = []
        while n > 0:
            binary.append(n % 2)
            n = n // 2
        
        # Добавление незначащих нулей до 32-ух
        binary.extend([0] * (32 - len(binary)))

        # преобразование обратно в десятичное представление в обратном порядке
        number, power = 0, 1
        for position in range(len(binary) - 1, -1, -1):
            number += binary[position] * power
            power *= 2
        return number


# ---- Вариант 2 ----

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = "0" * (32 - len(binary)) + binary
        return int(binary[::-1], 2)

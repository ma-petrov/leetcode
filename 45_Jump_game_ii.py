# https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: list[int]) -> int:

        # jumps - текущее кол-во прыжков. furthest - самая дальняя ячейка,
        # которая могла быть достигнута на момент ДО обхода i-го элемента
        # массива. current_furthest - самая дальнаяя ячейка на момент прыжка
        # с i-го элемента.
        jumps = furthest = current_furthest = 0

        for i in range(len(nums) - 1):

            # Если до ячейки i + x (x любое число) можно допрыгнуть минимум
            # за k шагов, то до ячейки i можно также допрыгнуть за k шагов.
            # Это значит, что если до предыщущего current_furthest (i + x)
            # можно допрыгнуть не менее чем за k шагов, то до нового
            # current_furthest также можно сделать k прыжков.
            current_furthest = max(current_furthest, i + nums[i])

            # Если i-ый элемент самый дальний, до которого можно было
            # допрыгнуть, то чтобы допрыгнуть до current_furthest нужно
            # сделать на один прыжок больше.
            if i == furthest:
                jumps += 1
                furthest = current_furthest

        return jumps

# https://leetcode.com/problems/generate-parentheses/


import collections


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        # Первый элемент кортежа - последовательность скобок,
        # второй элемент - кол-во открытых скобок.
        parenthesis = collections.deque([("(", 1)])

        for position in range(2, 2 * n + 1):

            # Из очереди берется фиксированное кол-во записей, которые были
            # добавлены на предыдущем шаге (каждый шаг - заполнение позиции
            # в строке).
            for _ in range(len(parenthesis)):
                p = parenthesis.popleft()
            
                # Если откртых скобок меньше, чем осталось добавить знаков,
                # то можно еще добавить открытую скобку.
                if 2 * n - position > p[1]:
                    parenthesis.append((p[0] + "(", p[1] + 1))
                
                # Если есть открытые скобки, можно добавить закрытую скобку.
                if p[1] > 0:
                    parenthesis.append((p[0] + ")", p[1] - 1))

        return [p[0] for p in parenthesis]

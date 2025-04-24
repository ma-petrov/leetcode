# https://leetcode.com/problems/regular-expression-matching/


import collections


# i - индекс строки, pi - индекс паттерна
Step = collections.namedtuple("Step", ["i", "pi"])


class Solution:
    ASTERISK = "*"
    WILDCARD = "."

    def isMatch(self, s: str, p: str) -> bool:

        self.checked = set()
        self.steps = collections.deque([Step(i=0, pi=0)])

        while self.steps:

            for _ in range(len(self.steps)):

                step = self.steps.popleft()
                if step.i >= len(s) and step.pi >= len(p):
                    return True

                # Если встретился двойной символ паттерна (со "*")
                if step.pi < len(p) - 1 and p[step.pi + 1] == self.ASTERISK:

                    # Если встретился pattern ".*", то нужно проверить все
                    # варианты оставшихся подстрок s[l:], где l >= step.i,
                    # соответствуют ли они паттерну p[step.pi + 2:].
                    if p[step.pi] == self.WILDCARD:
                        for l in range(step.i, len(s) + 1):
                            self.append_step(i=l, pi=step.pi + 2)
                    
                    # Если встретился паттерн "<символ>*", то нужно проверить
                    # все варианты s[l:], где i >= step.i и s[i] == <символ>,
                    # соответствуют ли они паттерну p[step.pi + 2:], а также
                    # подстроку s[step:i], так-как кол-во символа в строке
                    # может быть 0.
                    else:

                        # Для нулевого кол-ва символа из паттерна:
                        self.append_step(i=step.i, pi=step.pi + 2)

                        for l in range(step.i + 1, len(s) + 1):
                            if s[l - 1] != p[step.pi]:
                                break

                            self.append_step(i=l, pi=step.pi + 2)

                # Если встретился простой паттерн, проверяется только
                # соответствие символа.
                elif (
                    step.i < len(s)
                    and step.pi < len(p)
                    and p[step.pi] in (self.WILDCARD, s[step.i])
                ):
                    self.append_step(i=step.i + 1, pi=step.pi + 1)

        return False

    def append_step(self, i: int, pi: int):
        # Проверяет, добавлялся ли шаг проверки (i, pi) в очередь. Если он
        # добавлялся, то не имеет смысла запускать эту ветку второй раз. Иначе
        # добавляется в очередь.

        if (i, pi) not in self.checked:
            self.checked.add((i, pi))
            self.steps.append(Step(i=i, pi=pi))

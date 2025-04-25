# https://leetcode.com/problems/regular-expression-matching/


import collections


# i - индекс строки, pi - индекс паттерна
Step = collections.namedtuple("Step", ["i", "pi"])


class Solution:
    ASTERISK = "*"
    WILDCARD = "?"

    def isMatch(self, s: str, p: str) -> bool:

        self.checked = set()
        self.steps = collections.deque([Step(i=0, pi=0)])

        while self.steps:

            for _ in range(len(self.steps)):

                step = self.steps.popleft()
                if step.i >= len(s) and step.pi >= len(p):
                    return True

                if step.pi >= len(p):
                    continue

                # Если встретился патерн "*", то нужно проверить все
                # варианты оставшихся подстрок s[l:], где l >= step.i,
                # соответствуют ли они паттерну p[step.pi + 1:].
                if p[step.pi] == self.ASTERISK:
                    for l in range(step.i, len(s) + 1):
                        self.append_step(i=l, pi=step.pi + 1)
                
                # Если встретился символ "?", то нужно проверить соответствие
                # подстроки s[step.i] и паттерну p[step.pi].
                elif p[step.pi] == self.WILDCARD:
                    self.append_step(i=step.i + 1, pi=step.pi + 1)

                # Если встретился обычный символ, то далее проверяется
                # подстрока на соответсвие подпатеерну из обычных символов.
                else:
                    pi = step.pi
                    while (
                        pi < len(p)
                        and p[pi] not in (self.WILDCARD, self.ASTERISK)
                    ):
                        pi += 1

                    subpattern = p[step.pi : pi]
                    substring = s[step.i : step.i + pi - step.pi]
                    
                    if subpattern == substring:
                        self.append_step(i=step.i + pi - step.pi, pi=pi)

        return False

    def append_step(self, i: int, pi: int):
        # Проверяет, добавлялся ли шаг проверки (i, pi) в очередь. Если он
        # добавлялся, то не имеет смысла запускать эту ветку второй раз. Иначе
        # добавляется в очередь.

        if (i, pi) not in self.checked:
            self.checked.add((i, pi))
            self.steps.append(Step(i=i, pi=pi))

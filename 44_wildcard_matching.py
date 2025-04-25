# https://leetcode.com/problems/wildcard-matching/


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
                
                
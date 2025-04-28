# https://leetcode.com/problems/combination-sum/


import collections, copy


class ItermediateResult:
    def __init__(self, combination: list, total: int):
        self.combination = combination
        self.total = total


class Solution:
    def combinationSum(
        self,
        candidates: list[int],
        target: int
    ) -> list[list[int] | None]:

        candidates = sorted(list(set(candidates)))
        intermediates = collections.deque(
            [
                ItermediateResult(combination=[candidate], total=candidate)
                for candidate in candidates
            ]
        )
        combinations = []

        while intermediates:
            for _ in range(len(intermediates)):
                intermediate = intermediates.popleft()

                if intermediate.total == target:
                    combinations.append(intermediate.combination)
                    continue

                for candidate in candidates:

                    # Элементы добавляются только в осортированном порядке, это
                    # гарантирует отсутствие дублей комбинаций.
                    if (
                        candidate >= intermediate.combination[-1]
                        and intermediate.total + candidate <= target
                    ):
                        combination = copy.deepcopy(intermediate.combination)
                        combination.append(candidate)
                        intermediates.append(
                            ItermediateResult(
                                combination=combination,
                                total=intermediate.total + candidate,
                            )
                        )
        
        return combinations

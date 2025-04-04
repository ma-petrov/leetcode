# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/


class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:

        # Наибольший (последний) индекс карты
        picked = {}
        min_consecutive = None

        for index, card in enumerate(cards):

            if card in picked:
                min_consecutive = min(
                    min_consecutive or len(cards),
                    index - picked[card] + 1,
                )

                # Так как минимально возможная длина 2, при нахождении такого
                # значения его можно сразу вернуть и не заканчивать проверку.
                if min_consecutive == 2:
                    return 2

            # Обновление последнего индекса
            picked[card] = index
        
        return min_consecutive or -1

# https://leetcode.com/problems/push-dominoes/


import collections


class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        # .L.R...LR..L..
        # LL.RR.LLRRLL..

        next_to_drop = collections.deque(
            position
            for position in range(len(dominoes))
            if (
                position - 1 >= 0
                and dominoes[position - 1] == "R"
                or position + 1 < len(dominoes)
                and dominoes[position + 1] == "L"
            )
        )
        visited = set(p for p, d in enumerate(dominoes) if d != ".")
        moved_dominoes = list(dominoes)

        while next_to_drop:
            moves = []

            for _ in range(len(next_to_drop)):
                position = next_to_drop.popleft()

                if position in visited or not (0 <= position < len(dominoes)):
                    continue
                
                visited.add(position)

                # Случай, когда на домино падают домино слева и справа,
                # то домино остается на месте.
                if (
                    position - 1 >= 0
                    and moved_dominoes[position - 1] == "R"
                    and position + 1 < len(dominoes)
                    and moved_dominoes[position + 1] == "L"
                ):
                    continue

                # Домино падает направо
                if (
                    position - 1 >= 0
                    and moved_dominoes[position - 1] == "R"
                ):
                    moves.append((position, "R"))
                    next_to_drop.append(position + 1)
                    continue

                # Домино падает налево
                if (
                    position + 1 < len(dominoes)
                    and moved_dominoes[position + 1] == "L"
                ):
                    moves.append((position, "L"))
                    next_to_drop.append(position - 1)
                    continue
            
            for move in moves:
                moved_dominoes[move[0]] = move[1]
        
        return "".join(moved_dominoes)

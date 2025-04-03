# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        self.board = board
        self.visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(i, j, word):
                    return True
        return False

    def search(self, i: int, j: int, word: str) -> bool:
        # Если оставшаяся часть слова пустая - значит найдено все слово.
        if not word:
            return True

        # Проверяет, что текущий элемент доски находится в границах массива,
        # элемент еще не посещен и элемент содержит первую букву оставшейся
        # части слова. Если условие не выполняется, значи дальше по текущему
        # пути слово найти нельзя.
        if not (
            0 <= i < len(self.board)
            and 0 <= j < len(self.board[0])
            and (i, j) not in self.visited
            and word[0] == self.board[i][j]
        ):
            return False

        self.visited.add((i, j))

        # Поиск оставшейся части слова. Если слово найдено хотя бы по одному
        # пути, то функция вернет True.
        word = word[1:]
        result = (
            self.search(i + 1, j, word)
            or self.search(i - 1, j, word)
            or self.search(i, j + 1, word)
            or self.search(i, j - 1, word)
        )
        self.visited.remove((i, j))
        return result

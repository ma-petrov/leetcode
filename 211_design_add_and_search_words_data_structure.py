# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class Node(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node:
                node[letter] = Node()
            node = node[letter]
        
        node.is_word = True

    def search(self, word: str, node: Node | None = None) -> bool:
        node = node if node is not None else self.root

        for index, letter in enumerate(word):

            # Если встретился символ ".", нужно выполнить проверку для
            # оставшейся части слова по всем потомкам
            if letter == ".":
                return any(
                    self.search(word[index + 1:], child)
                    for child in node.values()
                )

            # Если встретилась буква и ее нет среди потомков, значит такое
            # слово отсутсвует
            if letter not in node:
                return False

            node = node[letter]
        
        return node.is_word

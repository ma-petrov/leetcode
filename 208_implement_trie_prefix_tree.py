# https://leetcode.com/problems/implement-trie-prefix-tree/


class Node(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        
        for letter in word:
            if letter not in node:
                node[letter] = Node()
            node = node[letter]

        node.is_word = True

    def search(self, word: str) -> bool:
        last_node = self._last_node(word)
        return last_node is not None and last_node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._last_node(prefix) is not None
    
    def _last_node(self, prefix: str) -> Node | None:
        node = self.root
        for letter in prefix:
            if letter not in node:
                return None
            node = node[letter]
        return node

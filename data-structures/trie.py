class Node:
    def __init__(self):
        """
        If the character set is limited to only lowercase English alphabet.
        then the space of each node is O(26) => O(1)
        """
        self.children = {}
        self.terminal = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert_word(self, word: str) -> None:
        """
        Let n = the length of the word
        Time: O(n)
        Space: O(n) if the word doesn't exist, else O(1)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.terminal = True

    def contains_word(self, word: str) -> bool:
        """
        Let n = the length of the word
        Time: O(n)
        Space: O(1)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.terminal


if __name__ == "__main__":
    t = Trie()

    t.insert_word("dog")
    t.insert_word("apple")
    t.insert_word("app")

    assert t.contains_word("dog"), "expected dog"
    assert t.contains_word("app"), "expected app"
    assert t.contains_word("apple"), "expected apple"
    assert not t.contains_word("appl"), "did not expected appl"

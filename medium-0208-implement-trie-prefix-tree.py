class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Time: O(n) where n is the length of word
        Space: O(n * sizeof Node), in the worst case all n letters of word will require a Node to be inserted
        """
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]

        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Time: O(n) where n is the length of word
        Space: O(1)
        """

        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Time: O(n) where n is the length of prefix
        Space: O(1)
        """
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

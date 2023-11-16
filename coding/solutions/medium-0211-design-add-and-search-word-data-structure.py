class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """
        Let n = the length of the word to add
        Time: O(n)
        Space: O(n)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Let n = the length of the word to search
        Time: O()
        Space: O()
        """
        return self.search_helper(0, self.root, word)

    def search_helper(self, idx: int, root: TrieNode, word: str) -> bool:
        curr = root

        for i in range(idx, len(word)):
            char = word[i]
            if char == ".":
                for child in curr.children.values():
                    # For instance, if word is '.ab', then search for 'ab' on the first recursive call, 'b',
                    # on the second, and so on.
                    if self.search_helper(i + 1, child, word):
                        return True
                return False
            else:
                if char not in curr.children:
                    return False
                curr = curr.children[char]

        return curr.isWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

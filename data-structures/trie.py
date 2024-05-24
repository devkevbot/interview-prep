"""
Trie implementation

In this implementation, the alphabet of the tree is restricted to lowercase
English letters a-z.

Space: O(alphabet size * average word size * number of words)
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert_word(self, word: str) -> None:
        """
        Time:
        - O(m), where m is the key length.
        - In each iteration of the algorithm, we either examine or create a node
        in the trie till we reach the end of the key. This takes only mmm
        operations.

        Space:
        - O(m)
        - In the worst case newly inserted key doesn't share a prefix with the
        the keys already inserted in the trie. We have to add mmm new nodes,
        which takes us O(m) space.

        Algorithm:
        - Start at the root of the Trie
        - For each letter in the word
            - Create a TrieNode if the letter doesn't exist in the current node's children
            - Visited the node that was just inserted
        - Mark the last inserted node as a word
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.word = True

    def search_word(self, word: str) -> bool:
        """
        Time:
            - O(m)
            - In each step of the algorithm we search for the next key
              character. In the worst case the algorithm performs m operations.
        Space:
            - O(1)

        Algorithm:
        - Start at the root of the Trie
        - For each letter in the word
            - If the letter is not in current node's children, return false
            - Visited the node belonging to the letter
        - Return if the last found node is a word
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.word

    def search_prefix(self, prefix: str) -> bool:
        """
        Time:
            - O(m)
            - In each step of the algorithm we search for the next key
              character. In the worst case the algorithm performs m operations.
        Space:
            - O(1)

        Algorithm:
        - Start at the root of the Trie
        - For each letter in the word
            - If the letter is not in current node's children, return false
            - Visited the node belonging to the letter
        - Return true
        """
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True

    def remove_word(self, word: str):
        """
        Time: O(k) where k is the size of the word being removed

        Algorithm:
        - Start at the root of the Trie
        - For each letter in the word
            - If the letter is not in current node's children, return
            - Visited the node belonging to the letter
        - If the last node is a word, mark it as a non-word
        - If the last node has no children, set the last node to None
        """
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return
            curr = curr.children[letter]

        if curr.word:
            curr.word = False

        if len(curr.children) == 0:
            curr = None


if __name__ == "__main__":
    t = Trie()

    t.insert_word("foobar")
    assert t.search_word("foobar"), "expected to find the word 'foobar'"
    assert t.search_prefix("foo"), "expected to find the prefix 'foo'"

    t.insert_word("cat")
    assert t.search_word("cat"), "expected to find the word 'cat'"
    t.insert_word("car")
    assert t.search_word("car"), "expected to find the word 'car'"

    t.remove_word("ca")
    assert t.search_word("cat"), "expected to find the word 'cat'"
    assert t.search_word("car"), "expected to find the word 'car'"

    t.remove_word("cat")
    assert not t.search_word("cat"), "expected to not find the word 'cat'"
    assert t.search_word("car"), "expected to find the word 'car'"

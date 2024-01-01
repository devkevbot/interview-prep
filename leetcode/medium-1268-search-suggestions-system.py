import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False  # Not needed for this problem, but still good to include for completeness of the Trie
        self.suggestions = []


class Trie:
    def __init__(self, max_suggestions: int = 3):
        self.max_suggestions = max_suggestions
        self.root = TrieNode()

    def insert(self, product_name: str):
        """
        Let n = the length of the input `product_name`
        Let k = the max number of suggestions
        Time: O(n)
        Space: O(n * k) (nodes may need to be created)
        """
        curr = self.root

        for char in product_name:
            curr = curr.children[char]
            self.add_suggestion(curr, product_name)

        curr.isWord = True

    def insert_many(self, product_names: list[str]):
        """
        Let m = the length of the input `product_names`
        Let n = the max length of an input in `product_names`
        Let k = the max number of suggestions
        Time: O(m * n)
        Space: O(m * n * k) (nodes may need to be created)
        """
        for product_name in product_names:
            self.insert(product_name)

    def add_suggestion(self, node: TrieNode, product_name: str):
        """
        Let n = the length of the input `product_name`
        Time: O(1)
        Space: O(n)
        """
        if len(node.suggestions) < self.max_suggestions:
            node.suggestions.append(product_name)

    def get_suggestions(self, search_word: str) -> list[list[str]]:
        """
        Let n = the length of the input `search_word`
        Let k = the max number of suggestions
        Time: O(n)
        Space: O(n * k)
        """
        res = [[] for _ in range(len(search_word))]

        curr = self.root

        for i, char in enumerate(search_word):
            if char not in curr.children:
                break
            curr = curr.children[char]
            res[i] = curr.suggestions

        return res


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        products = sorted(products)

        trie = Trie()
        trie.insert_many(products)
        return trie.get_suggestions(searchWord)

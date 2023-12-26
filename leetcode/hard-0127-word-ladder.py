import collections


class Solution:
    @staticmethod
    def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
        """
        Let n = the length of each word in the word_list
        Let m = the total number of words in the word_list
        Time: O(n^2 * m)
        Space: O(n * m)
        """

        # O(m * n) space
        word_list = set(word_list)
        if end_word not in word_list:
            return 0

        # O(m * n) space
        visited = set(begin_word)
        # O(m * n) space
        queue = collections.deque([begin_word])

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        changes = 1

        # O(m) iterations
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end_word:
                    return changes

                # O(n)
                for i in range(len(word)):
                    # O(26)
                    for j in alphabet:
                        new_word = list(word)
                        new_word[i] = j
                        # O(n)
                        new_word = "".join(new_word)
                        # O(1)
                        if new_word in word_list and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
            changes += 1

        return 0

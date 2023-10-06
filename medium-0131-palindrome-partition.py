class BacktrackingSolution:
    def partition(self, s: str) -> list[list[str]]:
        """
        Let n = the length of s
        Time: O(n * 2^n)
        Space: O(n)
        """

        result = []
        partition = []

        def dfs(start: int):
            # Add partition to answer
            if start >= len(s):
                result.append(partition.copy())
                return

            # Generate all substrings starting from index `start`
            for end in range(start, len(s)):
                # Explore substrings which are palindromes
                if self.is_palindrome(s, start, end):
                    partition.append(s[start: end + 1])
                    dfs(end + 1)
                    partition.pop()

        dfs(0)
        return result

    def is_palindrome(self, s: str, start: int, end: int):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
        return True

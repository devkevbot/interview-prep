from typing import List


# Iterative approach
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = ["()"]

        if n == 1:
            return combs

        for _ in range(n - 1):
            new_combs = set()

            for comb in combs:
                for j in range(len(comb)):
                    new_combs.add(comb[:j] + "()" + comb[j:])
                combs = new_combs
        return combs


# Recursive approach with stack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Time: O(?), https://en.wikipedia.org/wiki/Catalan_number lol
                    https://leetcode.com/problems/generate-parentheses/solutions/10099/time-complexity-to-generate-all-combinations-of-well-formed-parentheses/
        Space: O(n), since we recurse at most 2n times and hold n values in the stack
        """

        stack = []
        res = []

        def backtrack(open_n, closed_n):
            # There are n pairs of parentheses, which means there are n open parentheses and n
            # closed parentheses.
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            # Since a closed parenthesis must always be paired with an open parentheses, we can only
            # add a closed parentheses if the count of closed is less than the count of open.
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# Recursive approach with string concatenation
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_n, closed_n, path):
            # There are n pairs of parentheses, which means there are n open parentheses and n
            # closed parentheses.
            if open_n == closed_n == n:
                res.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")

            # Since a closed parenthesis must always be paired with an open parentheses, we can only
            # add a closed parentheses if the count of closed is less than the count of open.
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")

        backtrack(0, 0, "")

        return res

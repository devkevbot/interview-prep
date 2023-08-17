from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """

        stack = []

        for symbol in tokens:
            if symbol == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(second + first)
            elif symbol == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif symbol == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(first * second)
            elif symbol == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                totally_an_integer = int(symbol)
                stack.append(totally_an_integer)

        return stack.pop()

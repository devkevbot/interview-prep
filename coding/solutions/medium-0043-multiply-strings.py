class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Let n = the length of num1
        Let m = the length of num2
        Time: O(n * m)
        Space: O(n + m)
        """
        if "0" in [num1, num2]:
            return "0"

        # Multiplying a n-length digit by an m-length digit has a max product of length n + m.
        res = [0] * (len(num1) + len(num2))

        # When multiplying by hand we work right-to-left, so we'll reverse the inputs to iterate through the
        # original digits right-to-left
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # i1 + i2 is the column that we place the digit in
                res[i1 + i2] += digit  # account for the previous carry
                res[i1 + i2 + 1] += res[i1 + i2] // 10  # carry
                res[i1 + i2] = res[i1 + i2] % 10  # digit

        res, beg = res[::-1], 0
        # While we have leading zeros...
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # Convert int back str
        res = map(str, res[beg:])
        return "".join(res)

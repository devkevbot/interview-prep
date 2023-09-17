class BruteForceSolution:
    @staticmethod
    def my_pow(x: float, n: int) -> float:
        """
        Let n = the input n
        Time: O(n)
        Space: O(1)
        """
        if n == 0:
            return 1

        if x == 0:
            return 0

        answer = 1

        if n > 0:
            while n > 0:
                answer *= x
                n -= 1
        else:
            while n < 0:
                answer /= x
                n += 1

        return answer


class IterativeBinaryExponentiationSolution:
    def my_pow(self, x: float, n: int) -> float:
        """
        Let n = the input n
        Time: O(log n)
        Space: O(1)
        """
        return self.binary_exp(x, n)

    @staticmethod
    def binary_exp(x: float, n: int) -> float:
        if n == 0:
            return 1

        # x^-n = (1/x)^n
        if n < 0:
            n = -1 * n
            x = 1.0 / x

        result = 1

        while n != 0:
            # n is odd, multiply once with the result, so we can reduce n by 1 to make n even
            if n % 2 == 1:
                result *= x
                n -= 1

            # Square x and reduce n by half, x^n = (x^2)^(n/2)
            x *= x
            n //= 2

        return result

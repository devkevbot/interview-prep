class Solution:
    def find_cheapest_price(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        """
        Let f = the number of flights
        Let k = the input k
        Let n = the number of nodes, the input n
        Time: O(f * k)
        Space: O(n)
        """

        prev_step_prices = [float("inf")] * n
        prev_step_prices[src] = 0

        for _ in range(k + 1):
            current_step_prices = prev_step_prices.copy()

            # source, dest, price
            for s, d, p in flights:
                if prev_step_prices[s] == float("inf"):
                    continue

                if prev_step_prices[s] + p < current_step_prices[d]:
                    current_step_prices[d] = prev_step_prices[s] + p

            prev_step_prices = current_step_prices

        return -1 if prev_step_prices[dst] == float("inf") else prev_step_prices[dst]

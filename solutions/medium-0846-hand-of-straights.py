import heapq
from collections import defaultdict


class Solution:
    @staticmethod
    def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
        """
        Let n = the size of the hand
        Let g = the group size
        Time: O(n * log n)
        Space: O(n)
        """

        # Since each hand must be of size group_size, if the number of cards
        # we have is not evenly divisible by the group_size, we're going to have leftover cards.
        if len(hand) % group_size:
            return False

        # Record how many of each card is in the hand.
        # O(n) time + space
        count = defaultdict(int)
        for n in hand:
            count[n] += 1

        # O(n) space
        min_h = list(count.keys())
        heapq.heapify(min_h)
        while min_h:
            # Find the next lowest card to start the group for the current hand.
            first = min_h[0]
            # Since each group must consist of consecutive card, we can search in the range
            # starting from whichever card started the hand.
            # O(g) time
            for i in range(first, first + group_size):
                if i not in count:
                    return False
                count[i] -= 1
                # If we run out of cards...
                if count[i] == 0:
                    # ...and the card is not at the top of the heap...
                    if i != min_h[0]:
                        # ...there's now a gap in cards, so we can't form a consecutive run.
                        return False
                    # O(log n) time
                    heapq.heappop(min_h)
        return True

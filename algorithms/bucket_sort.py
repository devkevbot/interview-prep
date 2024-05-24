"""
Bucket sort implementation
"""

from typing import List


def bucket_sort(arr: List[int]):
    """
    Algorithm:
    - Initialize a structure to hold the frequency of each value
    - Iterate through the inptu array and increment the frequency for each value
    - Initialize a write pointer that indicates where to insert the next element
    - Iterate through the frequencies
        - For each frequency, iterate frequency number of times
            - Overwrite the input array at the write pointer location with the value associated with the frequency
            - Increment the write pointer

    Time Complexity:
    - O(n) because we only ever iterate through each element once

    Space Complexity:
    - O(1)

    Example:
        Input: [2,1,2,0,0,2]
        Steps:
            1. Build the count table: [0, 0, 0]
            2. Iterate and build the frequencies: [2, 1, 3]
            3. Iterate through frequencies and overwrite the array:
               [0,1,2,0,0,2]
               [0,0,2,0,0,2]
               [0,0,1,0,0,2]
               [0,0,1,2,2,2]
    """

    counts = [0, 0, 0]

    for num in arr:
        counts[num] += 1

    pos = 0
    for index in range(len(counts)):
        for _ in range(counts[index]):
            arr[pos] = index
            pos += 1

    return arr


if __name__ == "__main__":
    nums = [2, 1, 2, 0, 0, 2]
    assert bucket_sort(nums) == [0, 0, 1, 2, 2, 2]

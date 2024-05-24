"""
Topological Sort Implementation
"""

from typing import List


def topological_sort(adj_list: List[set]) -> List[int]:
    no_dependencies = []

    # Use a queue (or other list, order doesn't matter) to keep track of
    # which nodes don't have any dependencies
    for i in range(len(adj_list)):
        if len(adj_list[i]) == 0:
            no_dependencies.append(i)

    # We'll add non-dependent nodes to our result array as we remove them
    result = []

    # Repeatedly remove dependencies until we've gone through all nodes
    # or there are no nodes that don't have dependencies
    while len(no_dependencies) > 0:
        curr = no_dependencies.pop()
        result.append(curr)

        # Remove the node as a dependency from all other nodes
        for i in range(len(adj_list)):
            s = adj_list[i]
            if curr in s:
                s.remove(curr)

                # If it has no more dependencies, we can add it to our results
                if len(s) == 0:
                    no_dependencies.append(i)

    if len(result) == len(adj_list):
        return result

    return []


if __name__ == "__main__":
    """
    0 (Strings):      {1}
    1 (Arrays):       {}
    2 (Linked Lists): {}
    3 (Recursion):    {}
    4 (DP):           {1,3,5}
    5 (Trees):        {2}
    """
    adj_list = [{1}, {}, {}, {}, {1, 3, 5}, {2}]

    print(topological_sort(adj_list))

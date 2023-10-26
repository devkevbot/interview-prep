from collections import defaultdict, deque


class Solution:
    @staticmethod
    def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
        """
        Let v = the number of courses
        Let e = the number of prerequisites
        Time: O(v + e)
        Space: O(v + e)
        """

        # 1. Create adjacency list
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)

        # 2. Create array which stores the count of incoming edges for each node
        in_degrees = [0] * num_courses
        for course, _ in prerequisites:
            in_degrees[course] += 1

        # 3. Enqueue nodes that don't have incoming edges
        queue = deque()
        for course in range(num_courses):
            if in_degrees[course] == 0:
                queue.append(course)

        # 4. Topological sort
        while queue:
            course = queue.popleft()
            for next_course in adj_list[course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        # 5. Return false if any nodes still have incoming edges
        for count in in_degrees:
            if count != 0:
                return False
        return True

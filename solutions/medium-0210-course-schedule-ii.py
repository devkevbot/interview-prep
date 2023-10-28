from collections import defaultdict, deque


class Solution:
    @staticmethod
    def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Let v = the number of courses
        Let e = the number of prerequisites
        Time: O(v + e)
        Space: O(v + e)
        """

        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)

        in_degrees = [0] * num_courses
        for course, _ in prerequisites:
            in_degrees[course] += 1

        queue = deque()
        for course in range(num_courses):
            if in_degrees[course] == 0:
                queue.append(course)

        top_sort = []
        while queue:
            course = queue.popleft()
            top_sort.append(course)
            for next_course in adj_list[course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        for count in in_degrees:
            if count != 0:
                return []

        return top_sort

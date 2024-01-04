class RecursiveSolution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """
        Let n = the total number of rooms
        Let k = the total number of keys
        Time: O(n + k)
        Space: O(n)
        """

        def dfs(i: int, visited: set[int]):
            # We have access to all rooms
            if len(visited) == len(rooms):
                return True

            for neighbour in rooms[i]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                if dfs(neighbour, visited):
                    return True

            return False

        initial_visited = {0}
        return dfs(0, initial_visited)


class IterativeSolution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """
        Let n = the total number of rooms
        Let k = the total number of keys
        Time: O(n + k)
        Space: O(n)
        """
        seen = [False] * len(rooms)
        seen[0] = True

        stack = [0]

        # At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  # While we have keys...
            node = stack.pop()  # get the next key 'node'
            for nei in rooms[node]:  # For every key in room # 'node'...
                if not seen[nei]:  # ... that hasn't been used yet
                    seen[nei] = True  # mark that we've entered the room
                    stack.append(nei)  # add the key to the todo list
        return all(seen)  # Return true iff we've visited every room

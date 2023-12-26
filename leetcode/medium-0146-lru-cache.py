class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        Time: O(1)
        Space: O(1)
        """

        self.capacity = capacity

        self.cache = {}

        # tail and head are sentinel nodes so that we can avoid
        # re-creating and deleting head and tail over and over
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Time: O(1)
        Space: O(1)
        """

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Time: O(1)
        Space: O(1)
        """

        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            node_to_delete = self.head.nxt
            self.remove(node_to_delete)
            del self.cache[node_to_delete.key]

    def add(self, node: ListNode) -> None:
        before_tail = self.tail.prev
        before_tail.nxt = node
        node.prev = before_tail
        node.nxt = self.tail
        self.tail.prev = node

    def remove(self, node: ListNode) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

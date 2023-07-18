class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d: tuple[int, int] = {}
        self.q = deque([])

    def get(self, key: int) -> int:
        val, uses = self.d.get(key, (-1, 0))
        if uses == 0:
            return -1
        self.q.append(key)
        self.d[key] = (val, uses + 1)
        return val

    def put(self, key: int, value: int) -> None:
        _, uses = self.d.get(key, (-1, 0))
        self.d[key] = (value, uses + 1)
        self.q.append(key)

        while self.capacity < len(self.d):
            key = self.q.popleft()
            val, uses = self.d[key]
            if uses == 1:
                del self.d[key]
            else:
                self.d[key] = (val, uses - 1)
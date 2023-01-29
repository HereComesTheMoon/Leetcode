class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.start = 0
        self.d: dict[int, dict[int, int]] = defaultdict(lambda: OrderedDict())
        self.uses: dict[int, int] = {}
        

    def get(self, key: int) -> int:
        times_used = self.uses.get(key, None)
        if times_used is None:
            return -1
        self.uses[key] += 1
        bucket = self.d[times_used]
        val = bucket[key]
        del bucket[key]
        if not bucket and times_used == self.start:
            self.start += 1
        self.d[times_used + 1][key] = val
        return val


    def put(self, key: int, value: int) -> None:
        times_used = self.uses.get(key, None)
        if times_used:
            self.d[times_used + 1][key] = value
            del self.d[times_used][key]
            if not self.d[times_used] and times_used == self.start:
                self.start += 1
            self.uses[key] += 1
            return

        if self.cap:
            self.uses[key] = 1
            self.d[1][key] = value
            self.start = 1
            self.cap -= 1
            return

        if not self.uses:
            return
        popped_key, _ = self.d[self.start].popitem(False)
        del self.uses[popped_key]
        self.uses[key] = 1
        self.d[1][key] = value
        self.start = 1

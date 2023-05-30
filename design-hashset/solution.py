import bisect

class MyHashSet:

    def __init__(self):
        self.vals = [float('inf')]
        

    def add(self, key: int) -> None:
        i = bisect.bisect_left(self.vals, key)
        if self.vals[i] == key:
            return
        self.vals = self.vals[:i] + [key] + self.vals[i:]
        

    def remove(self, key: int) -> None:
        i = bisect.bisect_left(self.vals, key)
        if self.vals[i] != key:
            return
        self.vals.pop(i)


    def contains(self, key: int) -> bool:
        i = bisect.bisect_left(self.vals, key)
        return self.vals[i] == key

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
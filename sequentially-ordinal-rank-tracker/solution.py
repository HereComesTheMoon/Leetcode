from bisect import insort

class SORTracker:

    def __init__(self):
        self.locs = []
        self.pos = 0
        

    def add(self, name: str, score: int) -> None:
        insort(self.locs, (-score, name))
        

    def get(self) -> str:
        self.pos += 1
        return self.locs[self.pos - 1][1]
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
class LUPrefix:
    def __init__(self, n: int):
        self.n = n
        self.done = [False for _ in range(n + 1)]
        self.val = 0


    def upload(self, video: int) -> None:
        self.done[video] = True
        

    def longest(self) -> int:
        while self.val < self.n and self.done[self.val + 1]:
            self.val += 1
        return self.val
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
class BrowserHistory:
    def __init__(self, homepage: str):
        self.hp = homepage
        self.hist = [self.hp]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.pos + 1]
        self.hist.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos - steps)
        return self.hist[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.hist) - 1, self.pos + steps)
        return self.hist[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
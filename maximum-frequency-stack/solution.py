class FreqStack:
    def __init__(self):
        self.freqs = {}
        self.stacks = collections.defaultdict(list)
        self.maxi = 0

    def push(self, val: int) -> None:
        freq = self.freqs.get(val, 0) + 1
        self.freqs[val] = freq
        if self.maxi < freq:
            self.maxi = freq
        self.stacks[freq].append(val)


    def pop(self) -> int:
        val = self.stacks[self.maxi].pop()
        self.freqs[val] -= 1
        if not self.stacks[self.maxi]:
            self.maxi -= 1
        return val
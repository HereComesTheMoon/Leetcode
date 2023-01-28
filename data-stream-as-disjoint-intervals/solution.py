from bisect import bisect

class SummaryRanges:

    def __init__(self):
        self.ivs = [[-2, -2], [10_002, 10_002]]
        

    def addNum(self, value: int) -> None:
        i = bisect(self.ivs, [value, 10_002])
        if value <= self.ivs[i-1][1]:
            return
        if value == self.ivs[i-1][1] + 1:
            self.ivs[i-1][1] += 1
            if self.ivs[i][0] == value + 1:
                self.ivs[i-1][1] = self.ivs[i][1]
                self.ivs = self.ivs[:i] + self.ivs[i + 1:]
            return    
        if value + 1 == self.ivs[i][0]:
            self.ivs[i][0] -= 1
            return
        self.ivs = self.ivs[:i] + [[value, value]] + self.ivs[i:]


    def getIntervals(self) -> List[List[int]]:
        return self.ivs[1:len(self.ivs)-1]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

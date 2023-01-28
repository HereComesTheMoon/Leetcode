from bisect import insort

class SummaryRanges:

    def __init__(self):
        self.nums = []
        

    def addNum(self, value: int) -> None:
        insort(self.nums, value)
        

    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []
        res = [[self.nums[0], self.nums[0]]]
        for x in self.nums[1:]:
            if x <= res[-1][1] + 1:
                res[-1][1] = x
            else:
                res.append([x, x])
        return res
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
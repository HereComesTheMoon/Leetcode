class MyCalendar:

    def __init__(self):
        self.ivs = []
        

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect(self.ivs, (start, end))
        if 0 < i and start < self.ivs[i-1][1]:
            return False
        if i < len(self.ivs) and self.ivs[i][0] < end:
            return False
        bisect.insort(self.ivs, (start, end))
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
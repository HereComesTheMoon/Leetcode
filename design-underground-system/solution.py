class UndergroundSystem:

    def __init__(self):
        self.using: Dict[int, Tuple[str, int]] = {}
        self.avg: Dict[Tuple[str, str], Tuple[int, float]] = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.using[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t0 = self.using[id]
        number_seen, prev_avg = self.avg.get((startStation, stationName), (0, 0.))
        new_avg = (number_seen * prev_avg + (t - t0)) / (number_seen + 1)
        new_val = (number_seen + 1, new_avg)
        self.avg[(startStation, stationName)] = new_val
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
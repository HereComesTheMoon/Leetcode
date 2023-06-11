class SnapshotArray:
    def __init__(self, length: int):
        self.d = [[(0,0)] for _ in range(length)]   
        self.id = 0   

    def set(self, index: int, val: int) -> None:
        self.d[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.d[index], snap_id, key=lambda x: x[0]) - 1
        return self.d[index][i][1]      


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
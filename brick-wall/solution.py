class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        c = collections.Counter()
        for row in wall:
            val = 0
            for i, x in enumerate(row):
                row[i] = val + x
                val = row[i]
            c.update(row)
        if len(c) == 1:
            return len(wall)
        [_, (_, count)] = c.most_common(2)
        return len(wall) - count
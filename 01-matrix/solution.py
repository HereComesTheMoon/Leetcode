class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque([])
        res = [ [None for _ in mat[0]] for _ in mat ]
        seen = set()
        for y, row in enumerate(mat):
            for x, val in enumerate(row):
                if val == 0:
                    q.append((x, y))
                    seen.add((x, y))
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                res[y][x] = steps
                for xx, yy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if not(0 <= x + xx < len(mat[0])):
                        continue
                    if not(0 <= y + yy < len(mat)):
                        continue
                    if (x + xx, y + yy) in seen:
                        continue
                    seen.add((x + xx, y + yy))
                    q.append((x + xx, y + yy))
            steps += 1
        return res

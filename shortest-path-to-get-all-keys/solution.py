from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        q = deque()
        seen = set()
        number_keys = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == '@':
                    starting_val = (x, y, frozenset())
                    q.append(starting_val)
                    seen.add(starting_val)
                if val.isalpha():
                    number_keys += 1
        assert number_keys % 2 == 0
        number_keys = number_keys // 2
        assert len(q) == 1

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                x, y, keys = q.popleft()
                for xx, yy in ((1,0),(0,1),(-1,0),(0,-1)):
                    xx = x + xx
                    yy = y + yy
                    if (xx, yy, keys) in seen:
                        continue
                    if not(0 <= xx < len(grid[0])):
                        continue
                    if not(0 <= yy < len(grid)):
                        continue
                    if grid[yy][xx] == '#':
                        continue
                    seen.add((xx, yy, keys))
                    match grid[yy][xx]:
                        case '.' | '@':
                            q.append((xx, yy, keys))
                        case _ if grid[yy][xx] in keys:
                            q.append((xx, yy, keys))
                        case _ if grid[yy][xx].islower():
                            if len(keys) == number_keys - 1:
                                return steps
                            new_val = (xx, yy, keys | { grid[yy][xx] })
                            q.append(new_val)
                            seen.add(new_val)
                        case _ if grid[yy][xx].lower() in keys:
                            q.append((xx, yy, keys))
                        case _:
                            pass
        return -1
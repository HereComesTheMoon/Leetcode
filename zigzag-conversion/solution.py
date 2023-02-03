class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = [ [] for _ in range(numRows) ]
        for c, y in zip(s, zigzag(numRows)):
            grid[y].append(c)
        grid = ["".join(row) for row in grid]
        return "".join(grid)


def zigzag(numRows: int) -> Generator[int, None, None]:
    if numRows == 1:
        while True:
            yield 0
    y = 0
    while True:
        for _ in range(numRows - 1):
            yield y
            y += 1
        for _ in range(numRows - 1):
            yield y
            y -= 1
        

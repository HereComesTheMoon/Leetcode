class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def nextIndex(i: int, j: int) -> tuple[int, int]:
            if j == 8:
                return (i + 1, 0)
            return (i, j + 1)

        def backtrack(i: int, j: int):
            if i == 9:
                return True
            ii, jj = nextIndex(i, j)
            if board[i][j] != '.':
                return backtrack(ii, jj)
            options = getOptions(board, i, j)
            if not options:
                return False
            for c in options:
                board[i][j] = c
                if backtrack(ii, jj):
                    return True
            board[i][j] = '.'
            return False

        backtrack(0, 0)          


def getOptions(board: List[List[str]], i: int, j: int) -> set[str]:
    row = { c for c in board[i] }
    column = { row[j] for row in board }
    i = (i // 3) * 3
    j = (j // 3) * 3
    indices = [
        (0,0), (0,1), (0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1), (2,2),
    ]
    box = { board[i + a][j + b] for a, b in indices }
    return set(map(str, range(1, 10))) - (row | column | box)
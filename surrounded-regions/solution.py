class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def rec(x: int, y: int):
            if x not in range(len(board[0])):
                return
            if y not in range(len(board)):
                return
            if board[y][x] != 'O':
                return
            board[y][x] = 'KEEP'
        

            rec(x + 1, y)
            rec(x - 1, y)
            rec(x, y + 1)
            rec(x, y - 1)
        
        for x in range(len(board[0])):
            rec(x, 0)
            rec(x, len(board) - 1)
        for y in range(len(board)):
            rec(0, y)
            rec(len(board[0]) - 1, y)
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'KEEP':
                    board[y][x] = 'O'
                elif board[y][x] == 'O':
                    board[y][x] = 'X'



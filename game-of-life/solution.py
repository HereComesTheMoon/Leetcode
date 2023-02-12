class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        DEAD = 0
        LIFE = 1
        BIRTH = -1
        DYING = 2
        adj = [
            (1,1),
            (1,0),
            (1,-1),
            (0,1),
            (0,-1),
            (-1,1),
            (-1,0),
            (-1,-1),
        ]
        def update_cell(x: int, y: int) -> int:
            count = 0
            for xx, yy in adj:
                if x + xx not in range(len(board[0])):
                    continue
                if y + yy not in range(len(board)):
                    continue                    
                count += 1 if 0 < board[y + yy][x + xx] else 0
            if board[y][x] == 0:
                if count == 3:
                    return BIRTH
                return DEAD
            elif board[y][x] == 1:
                if count == 2 or count == 3:
                    return LIFE
                return DYING
            assert False
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                board[y][x] = update_cell(x, y)
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 1 or board[y][x] == -1:
                    board[y][x] = 1
                else:
                    board[y][x] = 0



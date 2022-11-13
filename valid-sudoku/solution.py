class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            l = list(filt(row))
            if len(l) != len(set(l)):
                print(l)
                return False
        for coli in range(len(board)):
            l = list(filt(board[i][coli] for i in range(9)))
            if len(l) != len(set(l)):
                print(l)
                return False
        for boxi in range(9):
            i = (boxi // 3) * 3
            j = (boxi % 3) * 3
            l = list(filt((
                board[i][j],
                board[i][j+1],
                board[i][j+2],
                board[i+1][j],
                board[i+1][j+1],
                board[i+1][j+2],
                board[i+2][j],
                board[i+2][j+1],
                board[i+2][j+2],
            )))
            if len(l) != len(set(l)):
                print("Here")
                print(l)
                return False
        return True
            
            
        
def filt(it):
    for x in it:
        if x != '.':
            yield x
    return None
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        one = player1[0]
        two = player2[0]
        if 1 < len(player1):
            one += player1[1] * (1 + (player1[0] == 10))
            two += player2[1] * (1 + (player2[0] == 10))
        for k in range(2, len(player1)):
            if player1[k-1] == 10 or player1[k-2] == 10:
                one += player1[k] * 2
            else:
                one += player1[k]
            if player2[k-1] == 10 or player2[k-2] == 10:
                two += player2[k] * 2
            else:
                two += player2[k]
        if one == two:
            return 0
        if two < one:
            return 1
        else:
            return 2
                
        
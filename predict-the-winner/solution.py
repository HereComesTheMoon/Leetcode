class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @functools.cache
        def game(i, j, turn: bool):
            if j <= i:
                return 0
            if turn:
                return max(
                    nums[i] + game(i+1, j, False),
                    nums[j-1] + game(i, j-1, False)
                    )
            else:
                return min(
                    game(i+1, j, True),
                    game(i, j-1, True)
                )
        
        res = game(0, len(nums), True)
        return sum(nums) <= res * 2
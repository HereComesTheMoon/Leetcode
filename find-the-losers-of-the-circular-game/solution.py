class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        got = set()
        ball = 0
        for i in range(1, n + 2):
            if ball in got:
                break
            got.add(ball)
            ball = (ball + i*k) % n
        return [x + 1 for x in range(n) if x not in got]
                
            
        
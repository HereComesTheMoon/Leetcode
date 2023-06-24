class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        res = 0
        @functools.cache
        def rec(i: int, left: int, right: int) -> int:
            nonlocal res
            if right < left:
                return
            if left == right:
                res = max(res, left)
            if i == len(rods):
                return
            if left + right <= 2 * res:
                return
            pole = rods[i]
            rec(i + 1, left + pole, right - pole),
            rec(i + 1, left, right),
            rec(i + 1, left, right - pole)
        
        rec(0, 0, sum(rods))
        return res
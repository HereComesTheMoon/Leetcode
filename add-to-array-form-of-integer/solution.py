class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_int = 0
        power = 1
        for x in reversed(num):
            num_int += x * power
            power *= 10
        val = k + num_int
        res = []
        while val != 0:
            res.append(val % 10)
            val //= 10
        res.reverse()
        return res
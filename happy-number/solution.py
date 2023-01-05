class Solution:
    def isHappy(self, n: int) -> bool:
        walker = f(n)
        runner = f(f(n))
        while True:
            if runner == 1:
                return True
            if runner == walker:
                return False
            walker = f(walker)
            runner = f(f(runner))

def f(n: int) -> int:
    res = 0
    while n != 0:
        res += (n % 10)**2
        n = n // 10
    return res
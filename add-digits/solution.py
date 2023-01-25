class Solution:
    def addDigits(self, num: int) -> int:
        def helper(a: int) -> int:
            res = 0
            while a != 0:
                res += a % 10
                a = a // 10
            return res
        
        while 9 < num:
            num = helper(num)
        
        return num
        
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        a = 1
        b = maxSum

        def check(value: int) -> bool:
            count = -value
            if value > index:
                count += (value + value - index) * (index + 1) // 2
            else:
                count += (value + 1) * value // 2 + index - value + 1
            if value >= n - index:
                count += (value + value - n + 1 + index) * (n - index) // 2
            else:
                count += (value + 1) * value // 2 + n - index - value
            return count <= maxSum

        while a < b:
            mid = (a + b + 1) // 2
            if check(mid):
                a = mid
            else:
                b = mid - 1
        return a
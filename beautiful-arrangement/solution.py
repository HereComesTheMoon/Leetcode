class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        used = set()

        def rec(k: int):
            nonlocal count
            for i in range(1, n + 1):
                if k % i and i % k:
                    continue
                if i in used:
                    continue
                if k == n:
                    count += 1
                    continue
                used.add(i)
                rec(k + 1)
                used.remove(i)
        rec(1)
        return count
        

# 1,2,3
# 3,2,1
# 2,1,3

# 1,2
# 2,1

# 2,4,3,1
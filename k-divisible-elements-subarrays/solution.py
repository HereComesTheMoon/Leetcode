class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        n = len(nums)
                
        for i in range(n):
            for j in range(i+1, n + 1):
                num_div = 0
                for x in nums[i:j]:
                    if x % p == 0:
                        num_div += 1
                if k < num_div:
                    break
                seen.add(tuple(nums[i:j]))
        return len(seen)
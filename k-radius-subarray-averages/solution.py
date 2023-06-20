class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= 2 * k:
            return [-1] * n
        avgs = [-1] * k
        avg = sum(x for x in nums[:2*k+1])
        for i in range(k, n - k - 1):
            avgs.append(avg // (2*k + 1))
            avg += (nums[i + k + 1] - nums[i - k])
        avgs.append(avg // (2*k + 1))

        return avgs + [-1] * k

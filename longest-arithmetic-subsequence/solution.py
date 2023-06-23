class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for k, x in enumerate(nums):
            d[x].append(k)
        longest = 1
        step = 0
        while step <= (500 / longest):
            for sign in [-1, -1]:
                step *= sign
                for k, x in enumerate(nums):
                    test = d[x - step]
                    if test and test[0] < k:
                        continue
                    length = 0
                    while True:
                        test = d[x + step]
                        i = bisect.bisect(test, k)
                        if i == len(test):
                            longest = max(longest, length)
                            break
                        length += 1
                        x = x + step
                        k = test[i]
            step += 1
        return longest + 1
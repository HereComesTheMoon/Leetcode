class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        filtered = [[]]
        for x in nums:
            if minK <= x <= maxK:
                filtered[-1].append(x)
            elif filtered[-1]:
                filtered.append([])
        if not filtered[-1]:
            filtered.pop()
        
        def count_pairs(k: int) -> int:
            return k * (k - 1) // 2

        def split(vals, borders):
            prev = -1
            for k, x in enumerate(vals):
                if x in borders:
                    d = k - prev
                    prev = k
                    yield d
            yield len(vals) - prev

        def count(vals):
            counter = count_pairs(len(vals) + 1)
            a = sum(count_pairs(val) for val in split(vals, [minK]))
            print(a)
            b = sum(count_pairs(val) for val in split(vals, [maxK]))
            c = sum(count_pairs(val) for val in split(vals, [minK, maxK]))
            return counter - a - b + c

        return sum(count(vals) for vals in filtered)

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return ( v for (v, _) in Counter(nums).most_common(k) )
        
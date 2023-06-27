import heapq as pq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [ (nums1[0] + nums2[0], 0, 0) ]
        res = []
        seen = set()
        while heap and len(res) < k:
            _, l, r = pq.heappop(heap)
            res.append((nums1[l], nums2[r]))
            if l + 1 < len(nums1) and (l + 1, r) not in seen:
                seen.add((l+1,r))
                pq.heappush(heap, (nums1[l+1] + nums2[r], l + 1, r))
            if r + 1 < len(nums2) and (l, r+1) not in seen:
                seen.add((l,r+1))
                pq.heappush(heap, (nums1[l] + nums2[r+1], l, r + 1))

        return res
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a = 0
        b = len(arr)
        if k < arr[0]:
            return k

        while a < b:
            mid = (a + b) // 2
            # number of missing pos ints < arr[mid]
            if a == mid:
                break
            if arr[mid] - (mid + 1) < k:
                a = mid
            else:
                b = mid
        return k + a + 1

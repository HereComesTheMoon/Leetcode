class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        return all(d == arr[i] - arr[i-1] for i in range(1, len(arr)))
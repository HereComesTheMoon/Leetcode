class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
      return max(enumerate(arr), key=lambda l: l[1])[0]
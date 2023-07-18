class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        largest = ""
        for [h1,h2,m1,m2] in itertools.permutations(arr):
            h = int(f"{h1}{h2}")
            m = int(f"{m1}{m2}")
            if 0 <= h <= 23 and 0 <= m <= 59:
                largest = max(largest, f"{h1}{h2}:{m1}{m2}")
        return largest

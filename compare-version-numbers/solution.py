from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        one = version1.split(".")
        two = version2.split(".")
        for x, y in zip_longest(one, two, fillvalue="0"):
            x = int(x)
            y = int(y)
            if x < y:
                return -1
            if y < x:
                return 1
        return 0
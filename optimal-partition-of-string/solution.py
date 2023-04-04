class Solution:
    def partitionString(self, s: str) -> int:
        total = 1
        bucket = set()
        for c in s:
            if c in bucket:
                bucket = { c } 
                total +=1
                continue
            bucket.add(c)
        return total
    
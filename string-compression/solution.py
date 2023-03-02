class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0
        for group in groupby(chars):
            chars[pos] = group[0]
            pos += 1
            length = sum(1 for _ in group[1])
            if length == 1:
                continue
            for num in str(length):
                chars[pos] = num
                pos += 1           
        return pos
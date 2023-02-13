class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        counter = defaultdict(int)
        for i in range(len(s) + 1 - 10):
            counter[s[i:i+10]] += 1
        
        res = []
        for k, v in counter.items():
            if v <= 1:
                continue
            res.append(k)
        return res
        
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split = s.split()
        if len(pattern) != len(split):
            return False
        d = {}
        seen = set()
        for k in range(len(pattern)):
            if pattern[k] in d:
                if d[pattern[k]] != split[k]:
                    return False
            else:
                d[pattern[k]] = split[k]
                if split[k] in seen:
                    return False
                else:
                    seen.add(split[k])
        return True
        

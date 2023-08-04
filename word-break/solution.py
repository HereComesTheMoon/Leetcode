class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = max(map(len, wordDict))
        words = set(wordDict)
        
        @functools.cache
        def rec(i: int) -> bool:
            if i == len(s):
                return True
            for j in range(i + 1, i + n + 1):
                if s[i:j] in words and rec(j):
                    return True
            return False
        
        return rec(0)
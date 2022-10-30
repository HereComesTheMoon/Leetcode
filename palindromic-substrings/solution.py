class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for n in range(len(s)):
            for k in range(1, 1 + min(n, len(s) - 1 - n)):
                if s[n-k] != s[n+k]:
                    break
                else:
                    count += 1 
        for n in range(1, len(s)):
            for k in range(min(n, len(s) - n)):
                if s[n-1-k] != s[n+k]:
                    break
                else:
                    count += 1
                    
        
        return count
        
                    
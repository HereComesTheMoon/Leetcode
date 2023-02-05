class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        while i < min(len(s), len(p)):
            if p[i] == '*':
                break
            if p[i] != '?' and p[i] != s[i]:
                return False
            i += 1
        s = s[i:]
        p = p[i:]

        j = 1
        while 0 <= min(len(s), len(p)) - j:
            if p[-j] == '*':
                break
            if p[-j] != '?' and p[-j] != s[-j]:
                return False
            j += 1
        s = s[:len(s) + 1 - j]
        p = p[:len(p) + 1 - j]

        if not p:
            return not s
        
        parts = list(filter(lambda part: bool(part), p.split("*")))
        if not parts:
            return True

        def check(pattern: str, pos: int) -> bool:
            if len(s) - pos < len(pattern):
                return False
            for i in range(len(pattern)):
                if pattern[i] == '?' or pattern[i] == s[pos + i]:
                    continue
                return False
            return True

        i = 0
        j = 0
        while i < len(s):
            if len(parts) <= j:
                return True
            if check(parts[j], i):
                i += len(parts[j])
                j += 1
            else:
                i += 1
        return len(parts) <= j
                    

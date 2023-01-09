class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) <= 1:
            assert s
            return [[s]]
        res = []
        for k in range(len(s) - 1):
            if not is_palindrome(s[:k+1]):
                continue
            rec = self.partition(s[k+1:])
            res += [ [s[:k+1]] + part for part in rec ]
        if is_palindrome(s):
            res += [ [s] ]
        return res

def is_palindrome(s: str) -> bool:
    for k in range(len(s) // 2):
        if s[k] != s[-1-k]:
            return False
    return True
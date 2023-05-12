from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        used_odd = False
        res = 0
        for letter, amount in count.items():
            res += amount - (amount % 2)
            if amount % 2 == 1:
                used_odd = True
        
        return res + int(used_odd)
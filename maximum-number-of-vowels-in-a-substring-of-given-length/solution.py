class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = { 'a', 'e', 'i', 'o', 'u' }
        now = 0
        for x in s[:k]:
            if x in vowels:
                now += 1
        maxi = now
        for i in range(k, len(s)):
            now += s[i] in vowels
            now -= s[i-k] in vowels
            maxi = max(maxi, now)
        return maxi
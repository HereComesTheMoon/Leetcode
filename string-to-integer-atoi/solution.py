class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if not s:
            return 0
        if not s[0].isdigit():
            return 0
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        val = sign * int(s[:i])
        if val < - 2**31:
            val = -2**31
        if (2**31) - 1 < val:
            val = 2**31 - 1
        return val
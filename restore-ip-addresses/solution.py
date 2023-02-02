class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def rec(s: str, depth: int) -> List[str]:
            if not s:
                return []
            if depth == 0:
                if s[0] == '0' and 1 < len(s):
                    return []
                if int(s) < 256:
                    return [s]
                return []
            
            res = []

            if s[0] == '0':
                return [ '0.' + x for x in rec(s[1:], depth - 1) ]

            for k in range(min(3, len(s))):
                if 256 <= int(s[:k+1]):
                    break
                vals = rec(s[k + 1:], depth - 1)
                for val in vals:
                    res.append(s[:k+1] + '.' + val)
            return res

        return rec(s, 3)

class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for k in range(n-1):
            vals = [[num[0]]]
            for x in num[1:]:
                if x == vals[-1][-1]:
                    vals[-1].append(x)
                else:
                    vals.append([x])
        
            now = []
            for val in vals:
                now.append(str(len(val)))
                now.append(val[0])
            num = "".join(now)
        return num
            



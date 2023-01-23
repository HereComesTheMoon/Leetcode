class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for k in range(len(num) - 2):
            if num[k] == num[k+1] == num[k+2]:
                if num[k].isdigit():
                    if res == "" or int(num[k:k+3]) > int(res):
                        res = num[k:k+3]
        return res
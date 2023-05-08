class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        as_list = []
        while 0 < x:
            as_list.append(x % 10)
            x = x // 10
        return as_list == list(reversed(as_list))

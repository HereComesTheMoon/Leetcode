class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0
        for k, c in enumerate(s):
            if c == ')':
                val = stack.pop()
                if not stack:
                    stack.append(k)
                else:
                    longest = max(longest, k - stack[-1])
            else:
                stack.append(k)
        return longest


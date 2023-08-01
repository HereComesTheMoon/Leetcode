class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(c)
                case ')':
                    if not stack:
                        return False
                    if stack.pop() != '(':
                        return False
                case ']':
                    if not stack:
                        return False
                    if stack.pop() != '[':
                        return False
                case '}':
                    if not stack:
                        return False
                    if stack.pop() != '{':
                        return False
                case _:
                    assert False
        return not stack
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""
        stack = []
        k = 0
        while k < len(p) - 1:
            if p[k+1] == '*':
                stack.append(p[k:k+2])
                k += 2
            else:
                stack.append(p[k])
                k += 1
        if k == len(p) - 1:
            stack.append(p[-1])

        k = 0
        new_p = []
        while k < len(stack) - 1:
            if len(stack[k]) == 2:
                if stack[k] == stack[k+1] or stack[k+1] == '.*':
                    k += 1
                    continue
            new_p.append(stack[k])
            k += 1
        new_p.append(stack[-1])

        p = "".join(new_p)

        return match(s, p)


def match(s: str, p: str) -> bool:
    if p == "":
        return s == ""

    if len(p) == 1:
        assert p[0] != '*'
        if len(s) != 1:
            return False
        if p[0] == '.':
            return True
        return p[0] == s[0]

    if not s:
        if p[1] == '*':
            return match(s, p[2:])
        return False

    if p[1] == '*':
        if p[0] == '.' or p[0] == s[0]:
            return match(s[1:], p) or match(s, p[2:])
        return match(s, p[2:])
    if p[0] == '.' or p[0] == s[0]:
        return match(s[1:], p[1:])
    return False

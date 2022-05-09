class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            b, a = a, b
        carry = False
        result = [None] * len(a)

        for k, (x, y) in enumerate(zip(reversed(a), reversed("0" * (len(a) - len(b)) + b))):
            if x == y:
                result[k] = carry
                carry = x == "1"
            else:
                result[k] = not carry

        result = "".join(("1" if x else "0" for x in reversed(result)))
        if carry:
            return "1" + result
        return result

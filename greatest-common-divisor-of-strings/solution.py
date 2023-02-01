class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = gcd(len(str1), len(str2))
        for k in divisors(n):
            candidate = str1[:k]
            if str1 != candidate * (len(str1) // k):
                continue
            if str2 != candidate * (len(str2) // k):
                continue
            return candidate
        return ""



def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    match (x % 2, y % 2):
        case (0, 0):
            return 2 * gcd(x // 2, y // 2)
        case (0, 1):
            return gcd(x // 2, y)
        case (1, 0):
            return gcd(x, y // 2)
        case (1, 1):
            return gcd(x - y, y)

def divisors(n: int) -> Generator[int, None, None]:
    yield n
    for k in range(n // 2, 0, -1):
        if n % k == 0:
            yield k
        
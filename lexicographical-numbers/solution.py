class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def rec(k: int):
            if n < k:
                return
            yield k
            yield from rec(10 * k)

            if k % 10 == 9:
                return
            yield from rec(k + 1)

        return rec(1)
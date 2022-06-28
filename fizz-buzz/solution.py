class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        def helper(x: int):
            if x % 15 == 0:
                return "FizzBuzz"
            if x % 3 == 0:
                return "Fizz"
            if x % 5 == 0:
                return "Buzz"
            return str(x)

        return [helper(x) for x in range(1, n + 1)]

class Solution:
    digits_to_char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return self.rec(digits)
    
    def rec(self, digits: str) -> List[str]:
        if not digits:
            return [""]

        return [
            head + tail for head in self.digits_to_char[digits[0]] for tail in self.rec(digits[1:])
        ]

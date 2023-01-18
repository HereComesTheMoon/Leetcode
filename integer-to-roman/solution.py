d = [
    (('M', 1000), ('C', 100)),
    (('D', 500), ('C', 100)),
    (('C', 100), ('X', 10)),
    (('L', 50), ('X', 10)),
    (('X', 10), ('I', 1)),
    (('V', 5), ('I', 1)),
]

class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        for i, ((letter, val), (smaller_letter, smaller_val)) in enumerate(d):
            if num < val - smaller_val:
                continue
            times = num // val
            left = num % val
            if val - smaller_val <= left:
                res.append(times * letter + smaller_letter + letter)
                num = left +  smaller_val - val
            else:
                res.append(times * letter)
                num = left
        res.append(num * 'I')
        return "".join(res)

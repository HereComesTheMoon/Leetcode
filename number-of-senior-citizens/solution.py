class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 if 60 < int(row[11:13]) else 0 for row in details)
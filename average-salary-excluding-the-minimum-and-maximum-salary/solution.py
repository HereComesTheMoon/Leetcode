class Solution:
    def average(self, salary: List[int]) -> float:
        mini = float('inf')
        maxi = float('-inf')
        summ = 0
        for x in salary:
            mini = min(x, mini)
            maxi = max(x, maxi)
            summ += x
        return (summ - mini - maxi) / (len(salary) - 2)
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        bounds = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]
        mini = bounds[:]
        mini.sort()
        mini = sum(mini[:k-1])
        maxi = bounds[:]
        maxi.sort(reverse=True)
        maxi = sum(maxi[:k-1])
        return maxi - mini

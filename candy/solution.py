class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [ 1 for _ in ratings ]
        for k in range(1, n):
            if ratings[k-1] < ratings[k]:
                candies[k] = candies[k-1] + 1
                
        candies_back = [ 1 for _ in ratings ]
        ratings.reverse()
        for k in range(1, n):
            if ratings[k-1] < ratings[k]:
                candies_back[k] = candies_back[k-1] + 1
                
        candies_back.reverse()

        return sum(max(x,y) for x, y in zip(candies, candies_back))

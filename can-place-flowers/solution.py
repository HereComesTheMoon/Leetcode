class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        run = 1
        count = 0
        for x in flowerbed:
            if x == 1:
                count += max(0, (run - 1) // 2)
                run = 0
            else:
                run += 1
        count += max(0, run // 2)
        return n <= count
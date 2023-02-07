class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        basket = {}
        i = 0
        j = 1
        basket[fruits[i]] = 1
        
        max_fruit = 2

        while j < len(fruits):
            if fruits[j] in basket:
                basket[fruits[j]] += 1
            else:
                basket[fruits[j]] = 1
            while 3 <= len(basket):
                basket[fruits[i]] -= 1
                if basket[fruits[i]] == 0:
                    del basket[fruits[i]]
                i += 1
            j += 1
            max_fruit = max(max_fruit, j - i)
                
        return max_fruit
        

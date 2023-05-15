class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        i = 0
        j = 1
        seen = { cards[0] }
        res = float('inf')
        
        while j < n and cards[j] not in seen:
            seen.add(cards[j])
            j += 1
        if j == n:
            return -1
        
        while j < n:
            while cards[j] in seen:
                seen.remove(cards[i])
                i += 1
            res = min(res, j + 2 - i)
            while j < n and cards[j] not in seen:
                seen.add(cards[j])
                j += 1
                
        return res
            
            
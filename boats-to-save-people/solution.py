class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        a = 0
        b = len(people) - 1
        total = 0
        while a <= b:
            if limit < people[a] + people[b]:
                b -= 1
                total += 1
            else:
                a += 1
                b -= 1
                total += 1
        return total
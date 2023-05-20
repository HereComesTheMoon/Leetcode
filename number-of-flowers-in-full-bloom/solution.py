from bisect import bisect, bisect_left

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        started = [ row[0] for row in flowers ]
        ended = [ row[1] for row in flowers ]
        started.sort()
        ended.sort()
        for k, x in enumerate(people):
            i = bisect(started, x)
            j = bisect_left(ended, x)
            people[k] = i - j
        return people

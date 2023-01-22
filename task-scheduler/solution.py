from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        time = 0
        while d:
            left = len(d)
            for val, count in d.most_common(n + 1):
                d[val] -= 1
                if d[val] == 0:
                    del d[val]
            if d:
                time += n + 1
            else:
                time += left
        return time
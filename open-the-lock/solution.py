class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        deadends = { tuple(map(int, deadend)) for deadend in deadends }
        if (0,0,0,0) in deadends:
            return -1
        target = tuple(int(d) for d in target)
        seen = { (0,0,0,0) }

        q = collections.deque(((0,0,0,0),))
        steps = 0
        while q:
            for _ in range(len(q)):
                now = q.popleft()
                for (sign, i) in itertools.product((1,-1), range(4)):
                    n = now[:i] + ((now[i] + sign) % 10,) + now[i+1:]
                    if n in seen:
                        continue
                    seen.add(n)
                    if n in deadends:
                        continue
                    if n == target:
                        return steps + 1
                    q.append(n)
            steps += 1
        return -1

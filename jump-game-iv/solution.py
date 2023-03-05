class Solution:
    def minJumps(self, arr: List[int]) -> int:
        buckets = defaultdict(list)
        for k, x in enumerate(arr):
            buckets[x].append(k)
        q = deque([0])
        seen = { 0 }
        seen_vals = set()
        jumps = 0
        while q:
            n = len(q)
            for _ in range(n):
                pos = q.popleft()
                if pos == len(arr) - 1:
                    return jumps
                if 0 < pos and pos - 1 not in seen:
                    seen.add(pos - 1)
                    q.append(pos - 1)
                if pos < len(arr) - 1 and pos + 1 not in seen:
                    seen.add(pos + 1)
                    q.append(pos + 1)
                if arr[pos] in seen_vals:
                    continue
                seen_vals.add(arr[pos])
                for next_pos in buckets[arr[pos]]:
                    if next_pos in seen:
                        continue
                    seen.add(next_pos)
                    q.append(next_pos)

            jumps += 1
        


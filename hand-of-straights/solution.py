class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True

        d = {}
        for x in hand:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        while d:
            down = next(iter(d.keys()))
            while down - 1 in d:
                down -= 1

            next_down = None
            while True:
                for x in range(down, down + groupSize):
                    print(x)
                    if x not in d:
                        return False
                    d[x] -= 1
                    if d[x] == 0:
                        del d[x]
                    elif next_down is None:
                        next_down = x
                if next_down is None:
                    if down + groupSize in d:
                        down += groupSize
                        continue
                    break
                else:
                    down = next_down
                    next_down = None
        return True

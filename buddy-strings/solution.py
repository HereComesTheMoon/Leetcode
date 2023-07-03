class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        
        it = [i for i, (x, y) in enumerate(zip(s, goal)) if x != y]
        if len(it) != 2:
            return False
        i, j = it
        return s[i] == goal[j] and s[j] == goal[i]
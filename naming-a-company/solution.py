from string import ascii_lowercase

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffix = { c : set() for c in ascii_lowercase }

        for idea in ideas:
            suffix[idea[0]].add(idea[1:])
        
        total = 0
        for k, c1 in enumerate(ascii_lowercase):
            for c2 in ascii_lowercase[k + 1:]:
                both = len(suffix[c1] & suffix[c2])
                total += (len(suffix[c1]) - both) * (len(suffix[c2]) - both)

        return 2*total


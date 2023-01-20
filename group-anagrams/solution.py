class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: dict[str, List[str]] = {}
        for s in strs:
            key = "".join(sorted(list(s)))
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
        return [bucket for bucket in d.values()]
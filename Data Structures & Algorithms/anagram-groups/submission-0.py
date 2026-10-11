class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorted_s = sorted(s)
            letters = "".join(sorted_s)
            if letters not in groups:
                groups[letters] = []
            groups[letters].append(s)
        return list(groups.values())
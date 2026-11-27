from collections import Counter


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        countrs = {}
        for str in strs:
            countrs[str] = Counter(str)
        print(countrs)
        return [[]]


s = Solution()
s.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])

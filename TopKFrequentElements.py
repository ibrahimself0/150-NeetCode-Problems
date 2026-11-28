from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        return [num for num, count in counter.most_common(k)]


s = Solution()
s.topKFrequent([1, 2, 2, 3, 3, 3, 3], 2)

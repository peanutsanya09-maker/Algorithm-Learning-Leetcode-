from typing import List


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        m = len(nums)
        res = []
        for i in range(n):
            l,r = queries[i]
            cnt = 0
            len = r - l + 1
            cnt += len

from functools import cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        l = len(digits)

        @cache
        def dfs(pos, isLimit, isNum):
            if pos == len(s):
                return 1 if isNum else 0

            res = 0
            if not isNum:
                res = dfs(pos + 1, False, False)

            up = s[pos] if isLimit else '9'

            for d in digits:
                if d > up:
                    break
                res += dfs(
                    pos + 1,
                    isLimit and (d == up),
                    True
                )
            return res

        return dfs(0, True, False)
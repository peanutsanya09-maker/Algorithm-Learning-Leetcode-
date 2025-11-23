from functools import cache
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        upper = 10**n-1
        s = str(upper)

        @cache
        def dfs(pos,mask,is_limit,is_num):
            if pos == len(s):
                return 1 if is_num else 0

            res = 0

            if not is_num:
                res = dfs(pos+1,mask)

            up = int(s[pos]) if isLimit else 9

            for d in range(0,up+1):
                res += dfs(
                    pos + 1,
                    cnt + (1 if d != )
                )
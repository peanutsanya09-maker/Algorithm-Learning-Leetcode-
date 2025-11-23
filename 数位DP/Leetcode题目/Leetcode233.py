from functools import cache
class Solution:
    def countDigitOne(self,n:int)->int:
        s = str(n)

        @cache
        def dfs(pos,cnt,is_limit):
            if pos == len(s):
                return cnt
            res = 0
            up = int(s[pos]) if is_limit else 9

            for d in range(0,up+1):
                res += dfs(
                    pos + 1,
                    cnt +(1 if d == 1 else 0),
                    is_limit and (d == up)
                )
            return res
        return dfs(0,0,True)
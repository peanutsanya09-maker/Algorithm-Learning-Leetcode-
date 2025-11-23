from linecache import cache


def countNumbers(n):
    """
    统计[0,n]中满足条件的数字个数
    """
    s = str(n)

    @cache
    def dfs(pos,state,is_limit,is_num):
        """
        :param pos: 当前处理到第几位(从高位到低位，0-indexed)
        :param state: 题目相关的状态
        :param is_limit: 当前位是否n的约束
        :param is_num: 是否已经填写了数字
        """
        if pos == len(s):
            return 1 if is_num else 0

        res = 0

        # 可以跳过当前位-处理前导0
        if not is_num:
            res = dfs(pos+1,state,False,False)

        up = int(s[pos]) if is_limit else 9 #如果受限，是能到s[pos]
        low = 0 if is_num else 1 #如果还没填数字，最小从1开始

        for d in range(low,up+1):
            new_state = update_state(state,d)

            if is_valid(new_state,d):
                res += dfs(
                    pos+1,
                    new_state,
                    is_limit and(d == up),
                    True
                )
        return res
    return dfs(0,init_state,True,False)
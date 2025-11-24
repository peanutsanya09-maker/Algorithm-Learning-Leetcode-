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
        :param is_limit: 当前位是否n的约束：True:前面的数字都是上界对应的数字，当前最高就是上界位 。False：前面的比上界小，该位置可以填0-9
        :param is_num: 是否已经填写了数字:True：前面已经填了数字，当前位可以填0-9 False:前面都是前导0，该位置跳过
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
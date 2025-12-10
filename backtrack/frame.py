def backtrack(路径,选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        将该选择从列表中移除
        路径.add(选择)

        backtrack(路径,选择列表)

        路径.remove(选择)
        将该选择加入列表
        

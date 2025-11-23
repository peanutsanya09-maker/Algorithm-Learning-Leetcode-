class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> list[int]:
        total = n * (n + 1) // 2
        if target > total or target < -total or (total - target) % 2 != 0:
            return []

        sum1 = (total - target) // 2

        negated = set()
        for x in range(n, 0, -1):
            if x <= sum1:
                negated.add(x)
                sum1 -= x

        res = []
        for x in sorted(negated, reverse=True): 
            res.append(-x)
        for x in range(1, n + 1):
            if x not in negated:
                res.append(x)

        return res
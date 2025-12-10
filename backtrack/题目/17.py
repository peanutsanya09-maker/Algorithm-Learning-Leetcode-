from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        p = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(idx, path):
            if len(path) == len(digits):
                res.append(path)
                return
            letters = p[digits[idx]]
            for ch in letters:
                backtrack(idx + 1, path + ch)

        backtrack(0, "")
        return res
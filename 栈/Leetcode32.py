class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        n = len(s)
        res = 0
        for char in s:
            if char == ')':



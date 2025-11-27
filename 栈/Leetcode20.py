class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
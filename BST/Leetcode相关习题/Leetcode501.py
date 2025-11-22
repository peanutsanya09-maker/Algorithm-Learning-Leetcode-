# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res  = defaultdict(int)
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res[node.val] += 1
            inorder(node.right)
        inorder(root)
        max_count = max(res.values())
        return [key for key,count in res.items() if count == max_count]

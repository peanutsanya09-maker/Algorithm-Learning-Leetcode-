# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, val):
            curr = node
            while curr:
                if curr.val == val:
                    return curr
                elif val < curr.val:
                    return search(curr.left, val)
                else:
                    return search(curr.right, val)

        return search(root, val)
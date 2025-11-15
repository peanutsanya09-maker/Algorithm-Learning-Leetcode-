# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def delete(node, val):
            if not node:
                return None

            if val < node.val:
                node.left = delete(node.left, val)
            elif val > node.val:
                node.right = delete(node.right, val)
            else:
                if not node.left and not node.right:
                    return None
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left


                min_node = find_min(node.right)
                node.val = min_node.val
                node.right = delete(node.right, min_node.val)

            return node

        return delete(root, key)
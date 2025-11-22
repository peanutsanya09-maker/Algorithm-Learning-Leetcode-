# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #快慢指针解法
    def sortedListToBST1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        slow,fast = head,head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        #为了防止prev只有一个节点
        if prev:
            prev.next = None

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST1(head if prev else None)
        root.right = self.sortedListToBST1(slow.next)

        return root

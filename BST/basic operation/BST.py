from numpy.ma.core import left_shift
class TreeNode:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def search(self,val):
        #在BST中寻找值为val的节点
        def search2(node,val):
            if not node or node.val == val:
                return node
            if val < node.val:
                return search2(node.left,val)
            else:
                return self.search2(node.right,val)
        return search2(self.root,val)

    def search_iterative(self,val):
        #迭代版本查找
        curr = self.root
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def insert(self,val):
        def insert2(node,val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = insert2(node.left,val)
            elif val > node.val:
                node.right = insert2(node.right,val)
            return node
        insert2(self.root,val)

    def delete(self,val):
        def delete2(node,val):
            if not node:
                return None
            if val < node.val:
                node.left = delete2(node.left,val)
            elif val > node.val:
                node.right = delete2(node.right,val)
            else:
                if not node.left and not node.right:
                    return None

                if not node.left:
                    return node.right

                if not node.right:
                    return node.left

                min_node = self.find_min(node.right)
                node.val = min_node.val
                node.right = delete2(node.right,min_node.val)

            return node
        delete2(self.root,val)

    def find_min(self,node):
        while node.left:
            node = node.left
        return node

    def find_max(self,node):
        while node.right:
            node = node.right
        return node

    def inorder(self):
        #中序遍历(左-根-右）
        res = []
        def inorder2(node,res):
            if not node:
                return
            inorder2(node.left,res)
            res.append(node.val)
            inorder2(node.right,res)
        inorder2(self.root,res)
        return res

    def preorder(self):
        #前序遍历(根-左-右)
        res = []
        def preorder2(node,res):
            if not node:
                return
            res.append(node.val)
            preorder2(node.left,res)
            preorder2(node.right,res)
        preorder2(self.root,res)
        return res

    def postorder(self):
        #后序遍历（左-右-根）
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if not node:
            return
        self._postorder_helper(node.left, result)
        self._postorder_helper(node.right, result)
        result.append(node.val)









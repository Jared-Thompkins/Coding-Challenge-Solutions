class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def isSymmetric(self, root: TreeNode):
        return self.mirror(root, root)

    def mirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.mirror(t1.right, t2.left) and self.mirror(t1.left, t2.right)
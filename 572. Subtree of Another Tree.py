class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]):
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True




    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
            self.sameTree(root.right, subRoot.right))

        return False
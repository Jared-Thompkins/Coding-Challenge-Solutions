class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if root == None:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


s = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

inverted = s.invertTree(root)

# Root child node tests
print(inverted.val)
print(inverted.left.val)
print(inverted.right.val)
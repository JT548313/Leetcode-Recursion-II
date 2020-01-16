# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True

        val = root.val
        if val <= lower or val >= upper:
            return False

        if not validate(root.left, lower, val):
            return False
        if not validate(root.right, val, upper):
            return False
        return True

        return validate(root)



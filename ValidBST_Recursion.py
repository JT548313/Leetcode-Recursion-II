# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: Node) -> bool:
        if not root:
            return True

        def validate(root, lower = float('-inf'), upper = float('inf')):
            if not root:
                return True

            val = root.val
            if val <= lower or val >=upper:
                return False

            if not validate(root.left, lower, val):
                return False
            if not validate(root.right, val, upper):
                return False
            return True

        return validate(root)

test = Node(5)
test.left = Node(1)
test.right = Node(7)
test.left.right = Node(4)
test.left.right.left = Node(2)
test.left.right.right = Node(6)
test.right.right = Node(8)
s= Solution()
print(s.isValidBST(test))


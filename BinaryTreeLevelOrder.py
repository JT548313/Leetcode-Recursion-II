from typing import List

# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return None

        output = []
        parent_queue = [root]
        child_queue = []
        temp = []
        while parent_queue:
            node = parent_queue.pop(0)
            temp.append(node.val)

            if node.left:
                child_queue.append(node.left)
            if node.right:
                child_queue.append(node.right)

            if len(parent_queue) == 0:
                output.append(temp)
                temp = []
                if len(child_queue) > 0:
                    parent_queue.extend(child_queue)
                    child_queue = []

        return output

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)

s = Solution()
s.levelOrder(root)
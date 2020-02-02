from collections import deque
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
        level_queue = deque()
        level_queue.append(root)
        while level_queue:
            level_size = len(level_queue)
            level_array = []
            for _ in range(level_size):
                node = level_queue.popleft()
                level_array.append(node.val)

                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            output.append(level_array)

        return output

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)

s = Solution()
s.levelOrder(root)
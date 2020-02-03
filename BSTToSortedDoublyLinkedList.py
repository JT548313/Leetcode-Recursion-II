# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return None

        stack = [root]
        output = []
        visited = [root.val]

        while stack:
            node = stack[-1]

            if node.left and node.left.val not in visited:
                stack.append(node.left)
                visited.append(node.left.val)
                continue

            if node.right:
                n = stack.pop()
                output.append(n)
                stack.append(node.right)
                visited.append(node.right.val)

            if not node.right and node.val in visited:
                output.append(stack.pop())

        tree_size = len(output)
        for index in range(tree_size):
            output[index].right = output[index + 1 if index + 1 < tree_size else 0]
            output[index].left = output[index - 1 if index - 1 >= 0 else tree_size - 1]

        return output[0]


root = Node(2)
root.left = Node(1)
# root.right = Node(6)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right.left = None
# root.right.right = Node(9)

s = Solution()
print(s.treeToDoublyList(root))

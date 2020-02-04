from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0

        stack = [-1]
        maxArea = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxArea = max(maxArea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxArea = max(maxArea, heights[stack.pop()] * (len(heights) - stack[-1] -1))

        return maxArea

s = Solution()
h = [6, 7, 5, 2, 4, 5, 9, 3]
print(s.largestRectangleArea(h))
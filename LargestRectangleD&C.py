from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0

        min_num = min(heights)
        area = min_num * len(heights)
        index_min = heights.index(min_num)
        area = max(area,  self.largestRectangleArea(heights[0:index_min]),
                   self.largestRectangleArea(heights[index_min+1:len(heights)]))

        return area


s = Solution()
h = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
print(s.largestRectangleArea(h))


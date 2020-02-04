from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights:
            return 0

        number_of_bars = len(heights)

        output = []

        for i in range(number_of_bars):
            current_bar_height = heights[i]
            counter = 1
            for j in range(i, number_of_bars-1):
                if current_bar_height <= heights[j + 1]:
                    counter += 1
                else:
                    break
            for k in range(i, 0, -1):
                if current_bar_height <= heights[k - 1]:
                    counter += 1
                else:
                    break

            output.append(current_bar_height * counter)

        return max(output) if output and (max(output) > max(heights)) else max(heights)

heights = [5,5,1,7,1,1,5,2,7,6]
s= Solution()
print(s.largestRectangleArea(heights))
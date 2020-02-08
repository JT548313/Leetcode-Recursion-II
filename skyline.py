from typing import List

class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        n = len(buildings)
        if n == 0:
            return []

        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])

        # merge left and right skylines
        # and return the skyline
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):

        def update_skyline(x, y):
            if not output or output[-1][0] != x:
                output.append([x, y])
            else:
                output[-1][1] = y

        def append_skyline(pos, lst, size, y, cur_y):
            while pos < size:
                x, y = lst[pos]
                pos += 1
                if cur_y != y:
                    update_skyline(x, y)
                    cur_y = y

        left_size, right_size = len(left), len(right)
        pos_l, pos_r = 0, 0
        cur_y = left_h = right_h = 0
        output = []

        while pos_l < left_size and pos_r < right_size:

            point_l, point_r = left[pos_l], right[pos_r]

            if point_l[0] < point_r[0]:
                x, left_h = point_l
                pos_l += 1
            else:
                x, right_h = point_r
                pos_r += 1

            max_h = max(left_h, right_h)
            # check for skyline change
            if cur_y != max_h:
                update_skyline(x, max_h)
                cur_y = max_h

        # append rest of left skyline
        append_skyline(pos_l, left, left_size, left_h, cur_y)

        # append rest of left skyline
        append_skyline(pos_r, right, right_size, right_h, cur_y)

        return output




b = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
s = Solution()
print(s.getSkyline(b))

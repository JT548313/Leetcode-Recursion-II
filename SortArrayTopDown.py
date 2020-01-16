from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums

        pivot = int(len(nums) / 2)
        left_list = self.sortArray(nums[:pivot])
        right_list = self.sortArray(nums[pivot:])

        return self.merge(left_list, right_list)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_list = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] >= right[right_idx]:
                sorted_list.append(right[right_idx])
                right_idx += 1
            elif left[left_idx] < right[right_idx]:
                sorted_list.append(left[left_idx])
                left_idx += 1

        if len(left) > left_idx:
            sorted_list.append(left[left_idx:])

        if len(right) > right_idx:
            sorted_list.append(right[right_idx:])

        return sorted_list

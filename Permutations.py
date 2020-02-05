import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return 0

        response = []

        def backtrack(first = 0):
            if first == len(nums):
                response.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return response


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))

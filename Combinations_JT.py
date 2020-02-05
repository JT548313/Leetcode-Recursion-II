import copy
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:

        if n == 0:
            return None

        if k == 0:
            return None

        response = []

        def backtrack(counter=1, combination=[], x_number_list=[]):
            if counter == k + 1:
                return
            for i in [y for y in range(1, n + 1) if y not in x_number_list]:
                combination.append(i)
                x_number_list.append(i)
                if counter == k:
                    temp = copy.deepcopy(sorted(combination))
                    response.append(temp)
                else:
                    backtrack(counter + 1, combination, x_number_list)
                combination.pop()
                if counter != 1:
                    x_number_list.pop()

        backtrack()

        unique_data = [list(x) for x in set(tuple(x) for x in response)]

        return unique_data


s = Solution()
print(s.combine(4, 3))

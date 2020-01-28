from typing import List

# for i in range(1, n):
#     for j in [x for x in range(n) if x != i]:
#         for k in [x for x in range(n) if x not in [i, j]]:
#             for l in [x for x in range(n) if x not in [i, j, k]]:
#                 input = [i]
#                 input.append(j)
#                 input.append(k)
#                 input.append(l)
#                 response.append(input)


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:

        if n == 0:
            return None

        if k == 0:
            return None

        response = []

        def backtrack(counter=1, combination=[1], x_number_list=[]):
            if counter == k + 1:
                return
            for i in [y for y in range(1, n + 1) if y not in x_number_list]:
                combination.append(i)
                x_number_list.append(i)
                if counter == k:
                    response.append(self.combination)
                    combination.pop()
                else:
                    backtrack(counter + 1, combination, x_number_list)

        backtrack()
        return response


s = Solution()
print(s.combine(4,2))






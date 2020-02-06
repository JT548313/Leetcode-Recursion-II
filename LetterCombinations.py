from typing import List
import itertools


class Solution:
    def __init__(self):
        self.mappings = {'2': ['a', 'b', 'c'],
                         '3': ['d', 'e', 'f'],
                         '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],
                         '6': ['m', 'n', 'o'],
                         '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'],
                         '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return None

        response = []

        def divideAndConquer(number):

            count_of_digits = len(number)

            mid = int(count_of_digits/2)

            if mid == 0:
                return self.mappings.get(number[0])

            list1 = divideAndConquer(number[0:mid])
            list2 = divideAndConquer(number[mid:])

            combo = [''.join(tuple) for tuple in (list(itertools.product(list1,list2)))]
            return combo

        return divideAndConquer(digits)


digits = '243'
s = Solution()
print(s.letterCombinations(digits))

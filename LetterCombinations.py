import json
from typing import List


class Solution:
    def __init__(self):
        self.mappings = json.dump({'2': ['a', 'b', 'c'],
                              '3': ['d', 'e', 'f'],
                              '4': ['g', 'h', 'i'],
                              '5': ['j', 'k', 'l'],
                              '6': ['m', 'n', 'o'],
                              '7': ['p', 'q', 'r', 's'],
                              '8': ['t', 'u', 'v'],
                              '9': ['w', 'x', 'y', 'z']})

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return None


        def divideAndConquer(number):

            count_of_digits = len(number)

            mid = int(count_of_digits)/2

            if mid == 0:
                n = number
                return self.mappings.

            divideAndConquer(number[0:mid])
            divideAndConquer(number[mid:-1])









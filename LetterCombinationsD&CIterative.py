from collections import deque
from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return None

        phone = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

        count_of_digits = len(digits)
        if count_of_digits == 1:
            return phone.get(digits[0])

        queue = deque()
        queue.append(digits[0:count_of_digits // 2])
        queue.append(digits[count_of_digits // 2:])

        combo = []

        while queue:
            lst = queue.popleft()
            length = len(lst)

            if length == 1:
                temp = phone.get(lst[0])
                if not combo:
                    combo = temp
                else:
                    combo = [''.join(tuple) for tuple in (list(itertools.product(combo, temp)))]
            else:
                queue.append(lst[0:length // 2])
                queue.append(lst[length // 2:])

        return combo


digits = '243'
s = Solution()
print(s.letterCombinations(digits))

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return

        output = []
        start, close = n
        queue = [('', '(', start, close)]

        while queue:
            combo, p, start, close = queue.pop()

            if p == '(':
                start -= 1
            elif p == ')':
                close -= 1
            combo += p

            if start == 0 and close == 0:
                output.append(combo)
            else:
                if start > 0:
                    queue.append((combo, '(', start, close))
                if close > 0 and close > start:
                    queue.append((combo, ')', start, close))

        return output;


s = Solution()
s.generateParenthesis(4)

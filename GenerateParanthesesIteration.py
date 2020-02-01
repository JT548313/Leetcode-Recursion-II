from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return

        output = []
        open = n
        close = n
        queue = [('','(', open, close)]

        while queue:
            combo, p, open, close = queue.pop()

            if p == '(':
                open -= 1
            elif p == ')':
                close -= 1
            combo += p

            if open == 0 and close == 0:
                output.append(combo)
            else:
                if open > 0:
                    queue.append((combo, '(', open, close))
                if close > 0 and close > open:
                    queue.append((combo, ')', open, close))

        return output;
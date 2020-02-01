from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(combi, p, open, close):
            if p == '(':
                open -= 1
            elif p == ')':
                close -= 1
            combi += p

            if open == 0 and close == 0:
                output.append(combi)
            else:
                if open > 0:
                    generate(combi, '(', open, close)
                if close > 0 and close > open:
                    generate(combi, ')', open, close)

        if n == 0:
            return

        output = []
        open = n
        close = n
        generate('', '(', open, close)
        return output;

s= Solution()
print(s.generateParenthesis(3))






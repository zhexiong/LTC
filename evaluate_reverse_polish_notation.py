class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        oprands = []
        for i in tokens:
            if i in ['+','-','*','/']:
                op2 = oprands.pop()
                op1 = oprands.pop()
                if i == '+':
                    oprands.append(op1 + op2)
                elif i == '-':
                    oprands.append(op1 - op2)
                elif i == '*':
                    oprands.append(op1 * op2)
                else:
                    sign = -1 if (op1 > 0) ^ (op2 > 0) else 1
                    oprands.append(sign * (abs(op1) / abs(op2)))
            else:
                oprands.append(int(i))
        return oprands.pop()
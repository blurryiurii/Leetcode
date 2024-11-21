# https://leetcode.com/problems/evaluate-reverse-polish-notation/
def evalRPN(tokens: list[str]) -> int:
    ops = {"+" , "-", "*", "/"}
    stack = list()
    for token in tokens:
        if token in ops:
            arg1, arg2 = stack.pop(), stack.pop()
            if token == "+":
                res = arg2 + arg1
            elif token == "-":
                res = arg2 - arg1
            elif token == "*":
                res = arg2 * arg1
            else:
                res = int(arg2 / arg1)
            stack.append(res)
        else:
            stack.append(int(token))
    return stack[0]
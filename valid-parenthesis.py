# https://leetcode.com/problems/valid-parentheses/

# stack-based approach, since each closing parenthesis
# must have an opening parenthesis of same type
def isValid(s: str) -> bool:
    cto = {"}": "{", "]": "[", ")" : "("}
    stack = []
    for char in s:
        # if it's a closing parenthesis, try to pop it from the stack
        if char in cto:
            # if our closing parenthesis != top of our stack, bad string.
            if not stack or stack.pop() != cto[char]:
                return False
        # if it's opening, append it to stack
        else:
            stack.append(char)
    # we return true only if our stack is empty. if it's not empty,
    # there must be some opening parenthesis that wasn't closed
    return not stack
"""
Problem: Given a string made up of the
following brackets: () [] {}, determin
whether the brackets properl match.
[{}] --> Valid
(()()) --> Valid
{] --> Invalid
[()]))() --> Invalid
[]{}({}) --> Valid
"""
from __Classes import Stack

reverseB = {
    '[':']',
    ']':'[',
    '{':'}',
    '}':'{',
    '(':')',
    ')':'('
}
def isLeft(c):
    return c in '[{('
# From array
def areBracketsValid(bStr):
    stack = []
    for b in bStr:
        sIdx = len(stack)-1
        revB = reverseB[b]
        if isLeft(b):
            stack.append(b)
        elif sIdx < 0:
            return False
        elif stack[sIdx] != revB:
            return False
        else:
            stack.pop()
    return len(stack) == 0
# Using built Stack Class
def stackValid(bStr):
    bStack = Stack()
    for b in bStr:
        revB = reverseB[b]
        if isLeft(b):
            bStack.push(b)
        elif bStack.isEmpty() or bStack.pop() != revB:
            return False
    return bStack.isEmpty()


# testing
testCases = ['[{}]', '(()())', '{]', '[()]))()', '[]{}({})', '[]{}({})((']
print("= Array stack =============================")
for s in testCases:
    print(areBracketsValid(s))
print("= Stack ===================================")
for s in testCases:
    print(stackValid(s))
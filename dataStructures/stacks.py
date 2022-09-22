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


def areBracketsValid2(bStr):
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
    return True

print(areBracketsValid2('[{}]'))
print(areBracketsValid2('(()())'))
print(areBracketsValid2('{]'))
print(areBracketsValid2('[()]))()'))
print(areBracketsValid2('[]{}({})'))
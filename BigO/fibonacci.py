# Looking at fibonacci for Big O: O(2^n)
def fibBad(numb):
    # Base-case
    if numb == 0: return 0
    if numb == 1: return 1
    # The money
    return fibBad(numb - 1) + fibBad(numb - 2)


print(fibBad(9))

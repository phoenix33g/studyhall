# O(n)
def countDown(n):
    if n == 0:
        return print("-------------------------")
    return countDown(n-1)

# O(n)
def twoLoops(a):
    for _ in range(0,a):
        pass
    for _ in range(0,a):
        pass

# O(a+b)
def twoInputsAdd(a,b):
    for _ in range(0,a):
        pass
    for _ in range(0,b):
        pass

# O(a*b)
def twoInputsAdd(a,b):
    for _ in range(0,a):
        for _ in range(0,b):
            pass
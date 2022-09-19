# Bad Big O: O(n!)
def f(n):
    if n == 0:
        print("*********************")
        return
    for i in range(0,n):
        f(n-1)


f(3)


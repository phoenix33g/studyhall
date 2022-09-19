# Exploring Big O(n log n)
def nLogNFun(n):
    y = n
    while n > 1:
        n = n // 2
        for i in range(1,y):
            print(f"Iteration for O(n) {i} : O(log n) {n}")


nLogNFun(4)
# Not optimized
def fibNotO(numb):
    if (numb == 0) or (numb == 1):
        return numb
    else:
        return fibNotO(numb-1) + fibNotO(numb-2)

# Memoizing to optimize
def fib(numb, memo):
    if memo == None: memo = {"0": 0, "1": 1}
    if str(numb) in memo:
        return memo[str(numb)]
    else:
        memo[str(numb)] = fib(numb-1, memo) + fib(numb-2, memo)
        return memo[str(numb)]


num = 10
# Limited by Integer length:: num = 997
print(f"The fibonacci number for {num} is: {fib(num, None)}")

# Limited by Big O, O(2^N)
#print(f"The fibonacci number for {num} is: {fibNotO(num)}")
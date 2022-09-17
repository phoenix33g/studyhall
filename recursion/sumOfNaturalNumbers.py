def recSummation(numb):
    if(numb <= 1):
        return numb
    return numb + recSummation(numb - 1)

num = 10
print(recSummation(int(num)))
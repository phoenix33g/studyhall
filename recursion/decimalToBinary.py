def decimalToBinary(decNum, binStr):
    if(int(decNum) == 0):
        return binStr
    binStr = str(int(decNum) % 2) + binStr
    return decimalToBinary(int(decNum/2), binStr)


numb = 233
print(decimalToBinary(numb, ''))
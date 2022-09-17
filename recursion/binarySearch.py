# For sorted array of numbers
def binarySearch(arr, startPos, endPos, value):
    if(startPos > endPos):
        return -1
    midPos = int((endPos + startPos) / 2)
    if(value == arr[midPos]):
        # Value is Middle Position
        return midPos
    if(value < arr[midPos]):
        # Value is on the Left side
        return binarySearch(arr, startPos, midPos-1, value)
    # Value is on the Right side
    return binarySearch(arr, midPos+1, endPos, value)


searchFor = 19
A = [-12, -2, -1, 0, 3, 5, 10, 19, 213]
result = binarySearch(A, 0, len(A)-1, searchFor)
print(f"Value {searchFor} is found in position:{result}")
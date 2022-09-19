# Binary Search through and sorted array
def binarySearch(arr, start, end, find):
    # Base-case.. no more array
    if start > end: return "Can't find it"
    # Split in half and check Mid point
    mid = (start + end) // 2
    if arr[mid] == find: return "Position: " + str(mid)
    if find > arr[mid]:
        return binarySearch(arr, mid + 1, end, find)
    if find < arr[mid]:
        return binarySearch(arr, start, mid -1, find)



# Do the things
import random
arr = []
for _ in range(random.randint(0,50)):
    val = random.randint(0,100)
    if not val in arr:
        arr.append(val)

arr.sort()
print(" || ".join(str(val) for val in arr))

findMe = 12
print(f"The location of {findMe} is: {binarySearch(arr, 0, len(arr)-1, findMe)}")
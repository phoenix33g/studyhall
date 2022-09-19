# Exploration of Big O through merge sort:: O( n log  n )
def mergeSort(arr):
    # Base-case for empty array
    if len(arr) <= 1: return arr
    # Split array and sort
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    tempArr = []
    l = 0
    r = 0
    # While both sub-arrays have values, then try and merge them in sorted order
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            tempArr.append(left[l])
            l += 1
        else:
            tempArr.append(right[r])
            r += 1
    # Add the rest of the values from the left sub-array into the temp array
    if l < len(left):
        return tempArr + left[l:]
    # Add the rest of the values from the right sub-array into the temp array
    if r < len(right):
        return tempArr + right[r:]


# Create a array of random lenght and elements
import random
arr = []
for _ in range(random.randint(1,50)):
    val = random.randint(0,100)
    if not val in arr:
        arr.append(val)

print(arr)
print(mergeSort(arr))
# Sort an array using divide and conquer 
def mergeSort(arr, startPos, endPos):
    if startPos < endPos:
        midPos = int((endPos + startPos) / 2)
        mergeSort(arr, startPos, midPos)
        mergeSort(arr, midPos+1, endPos)
        merge(arr, startPos, midPos, endPos)
# Step by Step array merge
def merge(arr, startPos, midPos, endPos):
    tempArr = []
    i = startPos
    j = midPos +1
    # While both sub-arrays have values, then try and merge them in sorted order
    while i <= midPos and j <= endPos:
        if arr[i] <= arr[j]:
            tempArr.append(arr[i])
            i +=1
        else:
            tempArr.append(arr[j])
            j +=1
    # Add the rest of the values from the left sub-array into the temp array
    while i <= midPos:
        tempArr.append(arr[i])
        i +=1
    # Add the rest of the values from the right sub-array into the temp array
    while j <= endPos:
        tempArr.append(arr[j])
        j +=1
    # Update original Array
    for k in range(startPos, endPos+1):
        arr[k] = tempArr[k-startPos]


A = [-23, 45, 3, -44, 0, 9, 77, -2, 98, 4]
mergeSort(A, 0, len(A)-1)
print(f'{A}')
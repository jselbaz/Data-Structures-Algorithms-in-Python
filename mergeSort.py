def mergeSort(arr):
    if len(arr) == 1:
        return arr
        
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_res = mergeSort(left)
    right_res = mergeSort(right)
    
    return mergeHelper(left_res, right_res)
    
def mergeHelper(left_res, right_res):
    result = [None] * (len(left_res) + len(right_res))
    i = j = k = 0
    
    while i < len(left_res) and j < len(right_res):
        if left_res[i] <= right_res[j]:
            result[k] = left_res[i]
            i += 1
        else:
            result[k] = right_res[j]
            j += 1
        k += 1
    
    while i < len(left_res):
        result[k] = left_res[i]
        i += 1
        k += 1
    
    while j < len(right_res):
        result[k] = right_res[j]
        j += 1
        k += 1

    return result

numbers = [4, 5, 6, 1, 3, 7, 2]
print(mergeSort(numbers))
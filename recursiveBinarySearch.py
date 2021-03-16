def recursiveBinarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    result = recursive(arr, target, left, right)
    return result
    
def recursive(arr, target, left, right):
    if left > right:
        return "Target Not Found"
    
    mid = (left + right) // 2
    mid_element = arr[mid]
    
    if target == mid_element:
        return mid
    elif target < mid_element:
        right = mid - 1
        result = recursive(arr, target, left, right)
        return result
    else:
        left = mid + 1
        result = recursive(arr, target, left, right)
        return result
        
print(recursiveBinarySearch([1, 7, 12, 17, 21, 32, 39], 21))
print(recursiveBinarySearch([5, 10, 15, 20, 25], 17))        
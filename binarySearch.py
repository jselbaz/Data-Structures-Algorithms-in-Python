def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_element = arr[mid]
            
        if target == mid_element:
            return mid
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
        
    return "Target Not Found"
        
print(binarySearch([1, 7, 12, 17, 21, 32, 39], 19))
print(binarySearch([5, 10, 15, 20, 25], 15))
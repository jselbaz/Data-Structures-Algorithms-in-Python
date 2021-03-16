def quickSort(arr):
    recursiveQS(arr, 0, len(arr) - 1)
    return arr
    
def recursiveQS(arr, start, end):
        if start >= end:
            return
            
        pivot = start
        left = start + 1
        right = end
        
        while right >= left:
            if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
                arr[left], arr[right] = arr[right], arr[left]
            
            if arr[left] <= arr[pivot]:
                left += 1
                
            if arr[right] >= arr[pivot]:
                right -= 1
                
        arr[pivot], arr[right] = arr[right], arr[pivot]
        
        recursiveQS(arr, start, right - 1)
        recursiveQS(arr, right + 1, end)
        
numbers = [4, 5, 6, 1, 3, 7, 2]
print(quickSort(numbers))
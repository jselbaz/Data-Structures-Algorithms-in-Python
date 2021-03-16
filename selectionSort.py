def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
                
        arr[i], arr[min] = arr[min], arr[i]
        
arr = [20, 12, 10, 15, 2]
selectionSort(arr)

print(arr)
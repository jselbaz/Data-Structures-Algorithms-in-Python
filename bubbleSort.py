def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range (0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
arr = [39, 20, 17, 37, 12]
bubbleSort(arr)

print(arr)
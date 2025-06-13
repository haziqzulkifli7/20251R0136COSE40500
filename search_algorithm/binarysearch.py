def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 10, 23, 30, 45]
target = 30

result = binary_search(arr, target)

if result != -1:
    print('Element:', target)
    print("Found at index:", result)
else:
    print("Element not found")

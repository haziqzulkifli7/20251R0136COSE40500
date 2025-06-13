def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 7, 1, 9, 2]
target = 9

result = linear_search(arr, target)

if result != -1:
    print('Element:', target)
    print("Found at index:", result)
else:
    print("Element not found")

def quick_sort(arr, low, high):
    if low < high:

        part = partition(arr, low, high)

        quick_sort(arr, low, part - 1)
        quick_sort(arr, part + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [64, 25, 12, 22, 11]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

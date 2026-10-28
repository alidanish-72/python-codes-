def floor_ceil(arr, target):
    low, high = 0, len(arr) - 1
    floor_val = None
    ceil_val = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid], arr[mid]

        elif arr[mid] < target:
            floor_val = arr[mid]
            low = mid + 1

        else:
            ceil_val = arr[mid]
            high = mid - 1

    return floor_val, ceil_val


arr = [1, 3, 5, 7, 9]
print(floor_ceil(arr, 6))  # (5, 7)
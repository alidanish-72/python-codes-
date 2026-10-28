def search_insert(arr, target):
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


print(search_insert([1, 3, 5, 6], 5))  # 2
print(search_insert([1, 3, 5, 6], 2))  # 1
print(search_insert([1, 3, 5, 6], 7))  # 4
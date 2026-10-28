def count_occurrences(arr, target):
    def lower_bound():
        low, high = 0, len(arr)

        while low < high:
            mid = (low + high) // 2

            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low

    def upper_bound():
        low, high = 0, len(arr)

        while low < high:
            mid = (low + high) // 2

            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid

        return low

    return upper_bound() - lower_bound()


arr = [1, 2, 2, 2, 3, 4]
print(count_occurrences(arr, 2))  # 3
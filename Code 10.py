def subset_sum(arr, i, target):
    if target == 0:
        return True

    if i == len(arr):
        return False

    # Exclude current element
    if subset_sum(arr, i + 1, target):
        return True

    # Include current element
    return subset_sum(arr, i + 1, target - arr[i])


arr = [3, 4, 5, 2]
print(subset_sum(arr, 0, 9))  # True
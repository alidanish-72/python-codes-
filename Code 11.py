def first_occurrence(arr, target, i=0):
    if i == len(arr):
        return -1

    if arr[i] == target:
        return i

    return first_occurrence(arr, target, i + 1)


def last_occurrence(arr, target, i=0):
    if i == len(arr):
        return -1

    result = last_occurrence(arr, target, i + 1)

    if result != -1:
        return result

    if arr[i] == target:
        return i

    return -1


arr = [1, 2, 3, 2, 4, 2]
print(first_occurrence(arr, 2))  # 1
print(last_occurrence(arr, 2))   # 5
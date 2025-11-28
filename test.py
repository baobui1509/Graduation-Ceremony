def count(*args):
    result = {}
    for item in args:
        result[item] = result.get(item, 0) + 1
    return result

# Example:
# count(1,2,2,3) -> {1: 1, 2: 2, 3: 1}
print(count(1, 2, 2, 3))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
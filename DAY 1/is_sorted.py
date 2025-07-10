def is_sorted(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)


A = [1, 22, 58, 45, 36, 75, 29]
print(is_sorted(A))
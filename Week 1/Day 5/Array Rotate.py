def rotate_right(arr, k):
    n = len(arr)
    k = k % n  
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
print("Original:", arr)
print(f"Right Rotated by {k}:", rotate_right(arr, k))
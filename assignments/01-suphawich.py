
# Insertion Sort, O(n**2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

print("Insertion Sort:")
input = [5,2,4,6,1,3]
print("Before", input)
print("After:", insertion_sort(input))


# Merge Sort
def merge(left, right, p, r):
    new_arr = []
    i, j = 0, 0
    for k in range(p-1, r):
        left_v = left[i] if i < len(left) else float('inf')
        right_v = right[j] if j < len(right) else float('inf')
        if (left_v <= right_v and left_v != float('inf')):
            new_arr.append(left_v)
            i = i + 1
        elif (right_v != float('inf')):
            new_arr.append(right_v)
            j = j + 1
    return new_arr

def merge_sort(a, p, r):
    if p == r: return a
    q = (p + r)//2
    left = merge_sort(a[:q], p, q)
    right = merge_sort(a[q:], p, q)
    return merge(left, right, p, r)

print("Merge Sort:")
input = [5,2,4,6,1,3]
print("Before:", input)
print("After:", merge_sort(input, 1, len(input)))
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)


def heapify(arr, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  if l < n and arr[i] < arr[l]:
    largest = l
  if r < n and arr[largest] < arr[r]:
    largest = r
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)

def buildMapHeap(arr):
  n = len(arr)
  for i in range(n//2, -1, -1):
    heapify(arr, n, i)

def heapSort(arr):
  n = len(arr)
  buildMapHeap(arr)
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)

data = [4, 8, 9, 2, 1, 7, 5]
print("Quicksort Unsorted Array:")
print(data)
quickSort(data, 0, len(data) - 1)
print('Sorted Array in Ascending Order:')
print(data)

print("---------------------------")

data = [4, 8, 9, 2, 1, 7, 5]
print("Heapsort Unsorted Array:")
print(data)
heapSort(data)
print('Sorted Array in Ascending Order:')
print(data)
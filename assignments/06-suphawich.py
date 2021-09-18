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
  return array


def countingSort(array, place = 10):
  s = len(array)
  o = [0] * s
  c = [0] * 10

  # Store the count of each elements in count array
  for i in range(0, s):
    index = array[i] // place
    c[index % 10] += 1

  # Store the cummulative count
  for i in range(1, 10):
    c[i] += c[i - 1]

  # Find the index of each element of the original array in count array
  # place the elements in output array
  i = s - 1
  while i >= 0:
    index = array[i] // place
    o[c[index % 10] - 1] = array[i]
    c[index % 10] -= 1
    i -= 1

  for i in range(0, s):
    array[i] = o[i]

def radixSort(array):
  # Get maximum element
  max_element = max(array)

  # Apply counting sort to sort elements based on place value.
  place = 1
  while max_element // place > 0:
    countingSort(array, place)
    place *= 10


def bucketSort(array):
  bucket = []

  # Create empty buckets
  for i in range(len(array)):
    bucket.append([])

  # Insert elements into their respective buckets
  for j in array:
    index_b = int(10 * j)
    bucket[index_b].append(j)

  # Sort the elements of each bucket
  for i in range(len(array)):
    a = bucket[i]
    bucket[i] = quickSort(a, 0, len(a) - 1)

  # Get the sorted elements
  k = 0
  for i in range(len(array)):
    for j in range(len(bucket[i])):
      array[k] = bucket[i][j]
      k += 1
  return array

data = [4, 8, 9, 2, 1, 7, 5]
print(f"Counting unsorted data: {data}")
countingSort(data)
print(f"Counting sorted data: {data}")
print("---------------------------")
data = [121, 432, 564, 23, 1, 45, 788]
print(f"Radix unsorted data: {data}")
radixSort(data)
print(f"Radix sorted data: {data}")
print("---------------------------")
data = [.42, .32, .33, .52, .37, .47, .51]
print(f"Bucket unsorted data: {data}")
bucketSort(data)
print(f"Bucket sorted data: {data}")
arr = [6, 1, 5, 4, 2, 3, 3]
length = 6
sorted = False
temp = 0
j = 0

while not sorted:
  for i in range(length - j):
    if arr[i] > arr[i+1]:
      temp = arr[i+1]
      arr[i+1] = arr[i]
      arr[i] = temp
      sorted = True

  sorted = not sorted
  j= j + 1

print (arr)

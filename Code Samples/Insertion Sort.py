arr = [6, 1, 5, 4, 2, 3, 3]
key = 0
temp = 0

for i in range(1,7):
  key = arr[i] 
  j = i - 1

  while j >= 0 and arr[j] > key:
    temp = arr[j+1]
    arr[j+1] = arr[j]
    arr[j] = temp
    j = j - 1

print (arr)

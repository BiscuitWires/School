arr = [1, 2, 3, 4, 5, 6]
low = 0
up = 5
found = False

target = int(input("Enter the target number "))

while low <= up and not found:
  mid = (low + up) // 2
  if target == arr[mid]:
    print ("Target found")
    found = True
  elif target > arr[mid]:
    low = mid + 1
  else:
    up = mid - 1

if not found:
  print ("Target not found")

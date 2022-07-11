array = [1, 2, 3, 4, 5]

def push(arrName, element):
  global sp
  sp = len(arrName) + 1
  if sp == 4:
    print ("stack is full")
  else:
    sp = sp + 1
    arrName.append(element)

def pop(arrName):
  global sp
  sp = len(arrName)
  if sp >= 0:
    target = arrName[p - 1]
    sp = sp - 1
    return target

n1 = int(input("Enter first value"))
n2 = int(input("Enter second value"))
push(array, n1)
push(array, n2)

print("Array: ", array)
print("Item popped was", pop(array))
print(array[:p])

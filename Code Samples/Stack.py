array = [1, 2, 3, 4, 5]
sp = len(array) - 1

print("stack pointer is", sp)

def push(arrName, element):
  global sp
  if sp >= 5:
    print ("Stack is full")
  else:
    sp = sp + 1
    arrName.append(element)
    print (element, " was added")

def pop(arrName):
  global sp
  if sp >= 0 and sp <= 5:
    target = arrName[sp]
    sp = sp - 1
    return target
  else:
    print("Stack is empty")
  

n1 = int(input("Enter first value "))
n2 = int(input("Enter second value "))
push(array, n1)
push(array, n2)

print("Array: ", array)
print(pop(array), "was popped")
print(array[:sp + 1])

array = [1, 2, 3, 4, 5]
LENGTH = 6
bp = len(array) - 1
tp = 0

def enqueue(arrName, element):
  global tp, bp, LENGTH
  if len(arrName[tp:bp + 1]) >= LENGTH:
    print("Queue is full")
  else:
    bp = bp + 1
    arrName.append(element)
    print (element, " was enqueued")

  
def dequeue(arrName):
  global tp, bp, LENGTH
  if len(arrName[tp:bp + 1]) <= 0:
    print("Queue is empty")
  else:
    target = arrName[tp]
    tp = tp + 1
    return target

n1 = int(input("Enter first value "))
n2 = int(input("Enter second value "))
enqueue(array, n1)
enqueue(array, n2)

print("Array: ", array)
print(dequeue(array), "was dequeued")
print("queue", array[tp:bp + 1])
print("array", array)

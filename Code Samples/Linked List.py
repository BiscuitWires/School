class Node:
  def __init__(self, data):
    self.data = data
    self.pointer = None

class List:
  def __init__(self):
    self.root = None #Root node initialises as None, changes when first node is created

  def Create_begin(self, data): #Adds a node before the root node
    N = Node(data)
    N.pointer = self.root
    self.root = N

  def Create_end(self, data): #Adds a node after the root node
    N = Node(data)

    temp = self.root
    while temp.pointer != None:
      '''
      This loop finds the last node. Note that we check if temp.pointer is 
      equal to None and not temp is equal to None. This is so that temp has
      the value of the last node.
      '''
      temp = temp.pointer

    temp.pointer = N
    
  def Display(self):
    temp = self.root
    while temp != None:
      '''
      This loop goes through the all the nodes which is why we check if
      temp itself is equal to None. If we instead checked if temp.pointer
      was equal to None, we wouldn't print the last node
      '''
      print("Data:", temp.data)
      print("Pointer:", temp.pointer)
      temp = temp.pointer

#Example tests
l = List() #Creates a new linked list

l.Create_begin(10) 
'''Adds a node at the start, this is the root node, the pointer has a
value of None'''

l.Create_begin(20) 
'''This creates a new node which is added before the current root 
node (node with value 10). The pointer here gets the value of the 
previous root node (node with value 10) and is then set as the root
node.'''

l.Create_end(30) 
'''This creates a new node which is added after the last node (whichever
ends with None, in this case the node with value 10). Here we don't have
to shift any root nodes, just have to set the previous node's (node with
value 10) pointer to this new node. Root node is still the node with value
20.'''

l.Display()

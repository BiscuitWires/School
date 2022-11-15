class Node:
  def __init__(self, data):
    self.data = data
    self.pointer = None

class List:
  def __init__(self):
    self.root = None

  def Create(self, data):
    N = Node(data)
    N.pointer = self.root
    self.root = N

class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None
    
  def insert(self, value):
    print('value', value)
    if value < self.value:
      if self.left is None:
        self.left = BST(value)
        self.left.parent = self
        return self
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BST(value)
        self.right.parent = self
        return self
      else:
        self.right.insert(value)
        
n = int(input())

values = list(map(int, input().split()))
tree = BST(values[0])
output = []

for i in range(1, len(values)):
  parent = tree.insert(values[i])
  if parent:
    output.append(parent.value)
  print(output)

# class BST:
#   def __init__(self, value):
#     self.value = value
#     self.left = None
#     self.right = None
#     self.parent = None
    
#   def insert(self, value):
#     if value < self.value:
#       if self.left is None:
#         self.left = BST(value)
#         self.left.parent = self
#         return self
#       else:
#         return self.left.insert(value)
#     else:
#       if self.right is None:
#         self.right = BST(value)
#         self.right.parent = self
#         return self
#       else:
#         return self.right.insert(value)
        
# n = int(input())

# values = list(map(int, input().split()))
# sorted_values = sorted(values)
# if values == sorted(values):
#   print(' '.join(map(str, values[:-1])))
#   exit()
# if values == sorted(values, reverse=True):
#   print(' '.join(map(str, values[:-1])))
#   exit()

# tree = BST(values[0])
# output = []

# for i in range(1, len(values)):
#   parent = tree.insert(values[i])
#   if parent:
#     output.append(parent.value)
  
# print(' '.join(map(str, output)))


import bisect

def main():
    n = int(input())
    a = list(map(int, input().split()))

    sorted_list = []
    parent_map = {}

    for i in range(n):
        current = a[i]

        # Find the position to insert the current element in the sorted list
        pos = bisect.bisect(sorted_list, current)

        # Determine the parent of the current element
        if pos == len(sorted_list):
            # Current element is the largest so far
            if pos > 0:
                parent_map[current] = sorted_list[pos - 1]
        else:
            # There is a larger element, check if it has a left child
            if sorted_list[pos] in parent_map and parent_map[sorted_list[pos]] < current:
                # The larger element already has a left child
                if pos > 0:
                    parent_map[current] = sorted_list[pos - 1]
            else:
                # The larger element does not have a left child
                parent_map[current] = sorted_list[pos]

        # Insert the current element into the sorted list
        bisect.insort(sorted_list, current)

        # Print the parent of the current element, except for the first element
        if i > 0:
            print(parent_map[current], end=" ")

    print()

if __name__ == "__main__":
    main()


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
 
def new_node(value):
  return Node(value)
 
def find_depth_and_height(root, k):
  if root is None:
    return
  depth = -1
  height = -1
  queue = []
  queue.append(root)
  level = 0
  while queue:
    n = len(queue)
    for i in range(n):
      front_node = queue.pop(0)
      if front_node.data == k:
        depth = level
      if front_node.left:
        queue.append(front_node.left)
      if front_node.right:
        queue.append(front_node.right)
    level += 1
  height = level - depth - 1
  print("Depth:", depth)
  print("Height:", height)
 
def main():
  # Binary Tree Formation
  root = new_node(5)
  root.left = new_node(10)
  root.right = new_node(15)
  root.left.left = new_node(20)
  root.left.right = new_node(25)
  root.left.right.right = new_node(45)
  root.right.left = new_node(30)
  root.right.right = new_node(35)
 
  k = 25
 
  find_depth_and_height(root, k)
 
if __name__ == "__main__":
  main()

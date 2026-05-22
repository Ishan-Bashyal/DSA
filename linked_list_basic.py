class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

# Create two nodes:
node1 = Node(10)
node2 = Node(20)

# Link them together:
node1.next = node2
linked_list = LinkedList()
linked_list.head = node1
print(linked_list.head.data)
print(linked_list.head.next.data)
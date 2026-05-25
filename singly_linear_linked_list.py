class LinearSinglyLinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# Creating Nodes 
Head = LinearSinglyLinkedList(1)
A    = LinearSinglyLinkedList(2)
B    = LinearSinglyLinkedList(3)
C    = LinearSinglyLinkedList(4)

# Linking Nodes 
Head.next = A
A.next    = B
B.next    = C


# 1. Insert at Beginning 
def insert_at_beginning(head, val):
    new_node = LinearSinglyLinkedList(val)
    new_node.next = head # new node points to old head
    head = new_node # new node becomes new head
    return head # must return new head


# 2. Insert at End 
def insert_at_end(head, val):
    new_node = LinearSinglyLinkedList(val)

    if head is None:
        return new_node

    current = head
    while current.next: # traverse till last node
        current = current.next

    current.next = new_node # last node points to new node
    return head


# 3. Delete from Beginning 
def delete_from_beginning(head):
    if head is None:
        print("List is empty")
        return None

    print(head.val, "deleted from beginning")
    head = head.next # second node becomes new head
    return head


# 4. Delete from End 
def delete_from_end(head):
    if head is None:
        print("List is empty")
        return None

    if head.next is None:       # only one node in list
        print(head.val, "deleted from end")
        return None

    current = head
    while current.next.next: # stop at second last node
        current = current.next

    print(current.next.val, "deleted from end")
    current.next = None # second last node now points to None
    return head


# Traverse 
def traverse(head):
    current = head
    while current:
        print(current)
        current = current.next


# Display 
def display(head):
    current  = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next 
    print(" -> ".join(elements))


# Search 
def searching(head, val):
    current = head
    while current:
        if val == current.val:
            return True
        current = current.next
    return False


# Testing

print("Original list:")
display(Head)

# Insert at beginning
Head = insert_at_beginning(Head, 0)
print("\nAfter inserting 0 at beginning:")
display(Head)

# Insert at end
Head = insert_at_end(Head, 5)
print("\nAfter inserting 5 at end:")
display(Head)

# Delete from beginning
Head = delete_from_beginning(Head)
print("\nAfter deleting from beginning:")
display(Head)

# Delete from end
Head = delete_from_end(Head)
print("\nAfter deleting from end:")
display(Head)

# Search
print("\nSearching for 2:", searching(Head, 2))
print("Searching for 9:", searching(Head, 9))
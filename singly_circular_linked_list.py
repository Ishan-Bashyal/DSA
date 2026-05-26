class SinglyCircularLinkedList:
    def __init__(self, val, next=None):
        self.val  = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

# Creating Nodes
Head = SinglyCircularLinkedList(1)
A = SinglyCircularLinkedList(2)
B = SinglyCircularLinkedList(3)
C = SinglyCircularLinkedList(4)

# Linking Nodes (last node points back to Head)
Head.next = A
A.next = B
B.next = C
C.next = Head


# 1. Insert at Beginning
def insert_at_beginning(head, val):
    new_node = SinglyCircularLinkedList(val)

    if head is None:
        new_node.next = new_node    # points to itself
        return new_node

    # find last node
    current = head
    while current.next != head:
        current = current.next

    new_node.next = head           # new node points to old head
    current.next = new_node       # last node points to new node
    head = new_node       # new node becomes head
    return head


# 2. Insert at End
def insert_at_end(head, val):
    new_node = SinglyCircularLinkedList(val)

    if head is None:
        new_node.next = new_node    # points to itself
        return new_node

    current = head
    while current.next != head:     # traverse till last node
        current = current.next

    current.next = new_node        # last node points to new node
    new_node.next = head            # new node points back to head
    return head


# 3. Delete from Beginning
def delete_from_beginning(head):
    if head is None:
        print("List is empty")
        return None

    if head.next == head:           # only one node
        print(head.val, "deleted from beginning")
        return None

    # find last node
    current = head
    while current.next != head:
        current = current.next

    print(head.val, "deleted from beginning")
    current.next = head.next        # last node points to second node
    head = head.next        # second node becomes new head
    return head


# 4. Delete from End
def delete_from_end(head):
    if head is None:
        print("List is empty")
        return None

    if head.next == head:           # only one node
        print(head.val, "deleted from end")
        return None

    current = head
    while current.next.next != head:  # stop at second last node
        current = current.next

    print(current.next.val, "deleted from end")
    current.next = head             # second last node points back to head
    return head


# Traverse
def traverse(head):
    if head is None:
        print("List is empty")
        return
    current = head
    while True:
        print(current)
        current = current.next
        if current == head:         # stop when we reach head again
            break


# Display
def display(head):
    if head is None:
        print("List is empty")
        return
    current = head
    elements = []
    while True:
        elements.append(str(current.val))
        current = current.next
        if current == head:         # stop when we reach head again
            break
    print(" -> ".join(elements) + " -> (back to head)")


# Search
def searching(head, val):
    if head is None:
        return False
    current = head
    while True:
        if current.val == val:
            return True
        current = current.next
        if current == head:         # stop when we reach head again
            break
    return False


# Testing

print("Original list:")
display(Head)

Head = insert_at_beginning(Head, 0)
print("\nAfter inserting 0 at beginning:")
display(Head)

Head = insert_at_end(Head, 5)
print("\nAfter inserting 5 at end:")
display(Head)

Head = delete_from_beginning(Head)
print("\nAfter deleting from beginning:")
display(Head)

Head = delete_from_end(Head)
print("\nAfter deleting from end:")
display(Head)

print("\nTraverse:")
traverse(Head)

print("\nSearching for 2:", searching(Head, 2))
print("Searching for 9:", searching(Head, 9))
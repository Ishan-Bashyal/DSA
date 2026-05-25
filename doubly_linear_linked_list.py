class DoublyLinearLinkedList:
    def __init__(self, val, prev=None, next=None):
        self.val  = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)


# Creating Nodes
Head = DoublyLinearLinkedList(1)
A    = DoublyLinearLinkedList(2)
B    = DoublyLinearLinkedList(3)
C    = DoublyLinearLinkedList(4)

# Linking Nodes
Head.next = A
A.prev    = Head
A.next    = B
B.prev    = A
B.next    = C
C.prev    = B


# 1. Insert at Beginning
def insert_at_beginning(head, val):
    new_node      = DoublyLinearLinkedList(val)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    head = new_node
    return head


# 2. Insert at End
def insert_at_end(head, val):
    new_node = DoublyLinearLinkedList(val)

    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next  = new_node
    new_node.prev = current
    return head


# 3. Delete from Beginning
def delete_from_beginning(head):
    if head is None:
        print("List is empty")
        return None

    print(head.val, "deleted from beginning")
    head = head.next
    if head is not None:
        head.prev = None
    return head


# 4. Delete from End
def delete_from_end(head):
    if head is None:
        print("List is empty")
        return None

    if head.next is None:
        print(head.val, "deleted from end")
        return None

    current = head
    while current.next:
        current = current.next

    print(current.val, "deleted from end")
    current.prev.next = None
    return head


# Traverse Forward
def traverse_forward(head):
    current = head
    while current:
        print(current)
        current = current.next


# Traverse Backward
def traverse_backward(head):
    if head is None:
        return
    current = head
    while current.next:
        current = current.next
    while current:
        print(current)
        current = current.prev


# Display
def display(head):
    current  = head
    elements = []
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" <-> ".join(elements))


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

print("\nTraverse forward:")
traverse_forward(Head)

print("\nTraverse backward:")
traverse_backward(Head)

print("\nSearching for 2:", searching(Head, 2))
print("Searching for 9:", searching(Head, 9))
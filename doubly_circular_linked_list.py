class DoublyCircularLinkedList:
    def __init__(self, val, prev=None, next=None):
        self.val  = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)


# Creating Nodes
Head = DoublyCircularLinkedList(1)
A    = DoublyCircularLinkedList(2)
B    = DoublyCircularLinkedList(3)
C    = DoublyCircularLinkedList(4)

# Linking Nodes
Head.next = A
Head.prev = C       # head's prev points to last node

A.prev    = Head
A.next    = B

B.prev    = A
B.next    = C

C.prev    = B
C.next    = Head    # last node points back to head


# 1. Insert at Beginning
def insert_at_beginning(head, val):
    new_node = DoublyCircularLinkedList(val)

    if head is None:
        new_node.next = new_node    # points to itself
        new_node.prev = new_node
        return new_node

    last = head.prev                # last node is head.prev in circular

    new_node.next = head            # new node → old head
    new_node.prev = last            # new node → last node
    head.prev     = new_node        # old head → new node
    last.next     = new_node        # last node → new node
    head          = new_node
    return head


# 2. Insert at End
def insert_at_end(head, val):
    new_node = DoublyCircularLinkedList(val)

    if head is None:
        new_node.next = new_node
        new_node.prev = new_node
        return new_node

    last = head.prev                # last node is always head.prev

    last.next     = new_node        # last node → new node
    new_node.prev = last            # new node → last node
    new_node.next = head            # new node → head
    head.prev     = new_node        # head → new node
    return head


# 3. Delete from Beginning
def delete_from_beginning(head):
    if head is None:
        print("List is empty")
        return None

    if head.next == head:           # only one node
        print(head.val, "deleted from beginning")
        return None

    last          = head.prev       # find last node
    print(head.val, "deleted from beginning")
    head          = head.next       # second node becomes head
    head.prev     = last            # new head → last node
    last.next     = head            # last node → new head
    return head


# 4. Delete from End
def delete_from_end(head):
    if head is None:
        print("List is empty")
        return None

    if head.next == head:           # only one node
        print(head.val, "deleted from end")
        return None

    last          = head.prev       # last node is head.prev
    second_last   = last.prev       # second last node

    print(last.val, "deleted from end")
    second_last.next = head         # second last → head
    head.prev        = second_last  # head → second last
    return head


# Traverse Forward
def traverse_forward(head):
    if head is None:
        print("List is empty")
        return
    current = head
    while True:
        print(current)
        current = current.next
        if current == head:
            break


# Traverse Backward
def traverse_backward(head):
    if head is None:
        print("List is empty")
        return
    current = head.prev             # start from last node
    while True:
        print(current)
        current = current.prev
        if current == head.prev:    # stop when back at last node
            break


# Display
def display(head):
    if head is None:
        print("List is empty")
        return
    current  = head
    elements = []
    while True:
        elements.append(str(current.val))
        current = current.next
        if current == head:
            break
    print(" <-> ".join(elements) + " <-> (back to head)")


# Search
def searching(head, val):
    if head is None:
        return False
    current = head
    while True:
        if current.val == val:
            return True
        current = current.next
        if current == head:
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

print("\nTraverse forward:")
traverse_forward(Head)

print("\nTraverse backward:")
traverse_backward(Head)

print("\nSearching for 2:", searching(Head, 2))
print("Searching for 9:", searching(Head, 9))
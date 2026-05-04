# Maximum size of queue
MAX = 5

# Initialize queue with fixed size
queue = [0] * MAX

# front -> points to first element
# rear -> points to last element
# -1 means queue is empty
front = -1
rear = -1


# Enqueue (Insert element into queue)
def enqueue(value):
    global front, rear  # we modify global variables

    # Condition for FULL queue (circular condition)
    # If next position of rear equals front → no space left
    if (rear + 1) % MAX == front:
        print("Queue Overflow")
    else:
        # If queue is empty, initialize front
        if front == -1:
            front = 0

        # Move rear forward in circular manner
        rear = (rear + 1) % MAX

        # Insert value at rear position
        queue[rear] = value

        # Confirmation message
        print(value, "inserted")


# Dequeue (Remove element from queue)
def dequeue():
    global front, rear  # we modify global variables

    # Condition for EMPTY queue
    if front == -1:
        print("Queue Underflow")
    else:
        # Print the element being removed
        print(queue[front], "removed")

        # If only one element was present
        if front == rear:
            # Reset queue to empty state
            front = -1
            rear = -1
        else:
            # Move front forward in circular manner
            front = (front + 1) % MAX


# Display elements of queue
def display():

    # If queue is empty
    if front == -1:
        print("Queue is empty")
    else:
        # Start from front
        i = front

        # Traverse until rear
        while True:
            print(queue[i], end=" ")

            # Stop when rear is reached
            if i == rear:
                break

            # Move index circularly
            i = (i + 1) % MAX

        print()  # for new line


# ---------------- TESTING ----------------

# Insert elements
enqueue(10)
enqueue(20)
enqueue(30)

# Display queue
display()

# Remove one element
dequeue()

# Display again
display()

# Insert more elements (circular behavior)
enqueue(40)
enqueue(50)
enqueue(60)

# Final display
display()
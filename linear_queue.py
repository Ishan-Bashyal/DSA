MAX = 5
queue = [0] * MAX
front = -1
rear = -1

# Enqueue
def enqueue(value):
    global front, rear
    if rear == MAX - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear = rear + 1
        queue[rear] = value
        print(value, "Inserted")

# Dequeue
def dequeue():
    global front
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print(queue[front], "removed")
        front = front + 1

# Display
def display():
    if front == -1 or front > rear:
        print("Queue is empty")
    else:
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()

# Test
enqueue(10)
enqueue(20)
enqueue(30)
display()

dequeue()
display()
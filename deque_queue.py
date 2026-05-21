class Deque:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.deque = []

    def is_full(self):
        return len(self.deque) == self.capacity

    def is_empty(self):
        return len(self.deque) == 0

    # Add to front
    def add_front(self, value):
        if self.is_full():
            print("Deque Overflow")
        else:
            self.deque.insert(0, value)
            print(value, "added to front")

    # Add to rear
    def add_rear(self, value):
        if self.is_full():
            print("Deque Overflow")
        else:
            self.deque.append(value)
            print(value, "added to rear")

    # Remove from front
    def remove_front(self):
        if self.is_empty():
            print("Deque Underflow")
        else:
            print(self.deque[0], "removed from front")
            self.deque.pop(0)

    # Remove from rear
    def remove_rear(self):
        if self.is_empty():
            print("Deque Underflow")
        else:
            print(self.deque[-1], "removed from rear")
            self.deque.pop()

    # Peek front
    def peek_front(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            print("Front:", self.deque[0])

    # Peek rear
    def peek_rear(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            print("Rear:", self.deque[-1])

    # Display
    def display(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            print("Deque (front to rear):", self.deque)

d = Deque()

d.add_rear(10)
d.add_rear(20)
d.add_rear(30)
d.display()

d.add_front(5)       # adds to front
d.display()

d.remove_rear()      # removes 30
d.display()

d.remove_front()     # removes 5
d.display()

d.peek_front()
d.peek_rear()
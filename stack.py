class Stack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.stack = []

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.is_full():
            print("Stack Overflow: Cannot push", item)
        else:
            self.stack.append(item)
            print("Pushed:", item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Nothing to pop")
            return None
        item = self.stack.pop()
        print("Popped:", item)
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print("Top element:", self.stack[-1])
        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):", self.stack[::-1])


s = Stack()

while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter value to push: ")
        s.push(item)
    elif choice == "2":
        s.pop()
    elif choice == "3":
        s.peek()
    elif choice == "4":
        s.display()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid choice, try again")
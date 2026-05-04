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
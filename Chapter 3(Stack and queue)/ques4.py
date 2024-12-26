"""Question 4 : Queue via Stacks: Implement a MyQueue class which implements a queue using two
stacks."""

class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0: 
            return None
        return self.list.pop()

class QueueViaStack():

    def __init__(self):
        self.inStack = Stack()  # Stack to handle enqueue
        self.outStack = Stack()  # Stack to handle dequeue

    def enqueue(self, val):
        self.inStack.push(val)  # Add item to the inStack

    def dequeue(self):
        # Transfer elements to outStack only if it's empty
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()  # Remove the front element
        # Transfer elements back to inStack
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

# Test the implementation
customQueue = QueueViaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())  # OUTPUT = 1
customQueue.enqueue(4)
print(customQueue.dequeue())  # OUTPUT = 2

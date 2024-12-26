"""QUESTION 6 : Sort Stack: Write a program to sort a stack such that the smallest items are on the
top. You can use an additional temporary stack, but you may not copy the elements into any other
data structure (such as an array). The stack supports the following operations: push, pop, peek,
and is Empty."""

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def __str__(self):
        return str(self.stack)

def sort_stack(stack):
    temporary_stack = Stack()
    while not stack.is_empty():
        #Check for every element of the stack
        curr = stack.pop()
        #If the current value is less than the top of the temporary stack then pop the pek of the temporary stack and push it in the original stack
        while not temporary_stack.is_empty() and temporary_stack.peek() > curr:
            stack.push(temporary_stack.pop())

        temporary_stack.push(curr)

    # Transfer sorted elements back to the original stack : the smallest element is at the bottom of the stack and the largest is at top of the temporary stack
    while not temporary_stack.is_empty():
        stack.push(temporary_stack.pop())

    return stack

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(34)
    s.push(3)
    s.push(31)
    s.push(98)
    s.push(92)
    s.push(23)

    print("Original Stack:", s) #Original Stack: [34, 3, 31, 98, 92, 23]
    sorted_stack = sort_stack(s)
    print("Sorted Stack:", sorted_stack) #Sorted Stack: [98, 92, 34, 31, 23, 3]

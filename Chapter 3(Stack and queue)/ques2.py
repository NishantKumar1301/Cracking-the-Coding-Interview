"""QUESTION 2 :Three in One: Describe how you could use a single array to implement three 
stacks. Stack Min: How would you design a stack which, in addition to push and pop, has a 
function min which returns the minimum element? Push, pop and min should all operation 0(1) time."""

class MultiStackWithMin:
    def __init__(self, stackSize):
        self.numberOfStack = 3
        self.custList = [0] * (self.numberOfStack * stackSize)
        self.stackSize = stackSize
        self.sizes = [0] * self.numberOfStack
        self.minStack = [[] for _ in range(self.numberOfStack)]  # Separate min stacks for each stack

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackSize

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1

    def push(self, stackNum, val):
        if self.isFull(stackNum):
            return "Stack is Full"
        else:
            self.sizes[stackNum] += 1
            self.custList[self.indexOfTop(stackNum)] = val
            if not self.minStack[stackNum] or val <= self.minStack[stackNum][-1]:
                self.minStack[stackNum].append(val)

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return "Stack is empty"
        else:
            top_index = self.indexOfTop(stackNum)
            val = self.custList[top_index]
            self.custList[top_index] = 0
            self.sizes[stackNum] -= 1
            if val == self.minStack[stackNum][-1]:
                self.minStack[stackNum].pop()
            return val

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            return "Stack is empty"
        else:
            return self.custList[self.indexOfTop(stackNum)]

    def getMin(self, stackNum):  
        if self.isEmpty(stackNum):
            return "Stack is empty"
        else:
            return self.minStack[stackNum][-1]


# Example Usage
stack = MultiStackWithMin(3)
stack.push(0, 5)
stack.push(0, 2)
stack.push(0, 8)
print(stack.getMin(0))  # Output: 2
stack.pop(0)
print(stack.getMin(0))  # Output: 2
stack.pop(0)
print(stack.getMin(0))  # Output: 5
stack.push(1, 7)
stack.push(1, 3)
stack.push(1, 6)
print(stack.getMin(1))  # Output: 3
print(stack.getMin(2)) #Stack is empty as no element have been pushed in the stack 3 yet
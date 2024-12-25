"""QUESTION 3 : Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this. Set Of Stacks should be composed of several stacks and
should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() 
should behave identically to a single stack (that is, pop () should return the same values as it would if there
were just a single stack). FOLLOW UP Implement a function popAt ( int index) which performs a pop operation on a 
specific sub-stack."""

class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum capacity for each stack
        self.stacks = []  # List to hold multiple stacks

    def __str__(self):
        return str(self.stacks)  

    def push(self, plate):
        # Add a plate to the last stack if it's not full; otherwise, create a new stack
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(plate)
        else:
            self.stacks.append([plate])

    def pop(self):
        # Remove plates from the last non-empty stack
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
        
    def pop_at(self, stackNum):
        # Remove plates from a specific stack if the stack is not empty
        if stackNum < len(self.stacks) and len(self.stacks[stackNum]) > 0:
            return self.stacks[stackNum].pop()
        else:
            return None


plates = PlateStack(3)
for i in range(1, 11):
    plates.push(i)
print(plates)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
print(plates.pop())  # 10
print(plates)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(plates.pop_at(1)) # OUTPUT = 6
print(plates) # [[1, 2, 3], [4, 5], [7, 8, 9]]

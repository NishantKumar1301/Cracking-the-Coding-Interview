#QUESTION 1: Three in One: Describe how you could use a single array to implement three stacks.

class MultiStack:
    def __init__(self,stackSize):
        self.numberOfStack = 3 
        self.stackSize = stackSize 
        self.sizes = [0]*self.numberOfStack  # This contains the size of each stack
        self.custList=[0]*(stackSize*self.numberOfStack) #This contains the common overall list
        

    def isFull(self,stackNum):
        if self.sizes[stackNum]==self.stackSize:
            return True
        else:
            return False
        
    def isEmpty(self,stackNum):
        if self.sizes[stackNum]==0:
            return True
        else:
            return False

    def topIndexOfStack(self,stackNum):
        offset = stackNum*self.stackSize
        return offset+self.sizes[stackNum]-1 #Example if stacknum =0 then offset = 0, top = 0+3-1=2
    
    def push(self,stackNum,val):
        if self.isFull(stackNum):
            return "The Stack is Full"
        else:
            self.sizes[stackNum]+=1
            self.custList[self.topIndexOfStack(stackNum)]=val
            

    def pop(self ,stackNum):
        if self.isEmpty(stackNum):
            return "The stack is empty"
        else:
            value = self.custList[self.topIndexOfStack(stackNum)]
            self.custList[self.topIndexOfStack(stackNum)]==0
            self.sizes[stackNum]-=1
            return value

    def peek(self,stackNum):
        if self.isEmpty(stackNum):
            return "The stack is empty"
        else:
            return self.custList[self.topIndexOfStack(stackNum)]

stack = MultiStack(6)
print(stack.isEmpty(1))
print(stack.isFull(2))
stack.push(0,3)
stack.push(0,2)
stack.push(1,1)
stack.push(2,3)
stack.push(2,2)
stack.push(1,10)
print(stack.isEmpty(2))
print(stack.pop(1))
print(stack.peek(1))
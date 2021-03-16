class MaxStack:
    
    def __init__(self):
        self.stack = []
        self.max = []
        
    def push(self, x):
        self.stack.append(x)
        
        if self.max:
            if x >= self.max[-1]:
                self.max.append(x)
        else:
            self.max.append(x)
        
    def pop(self):
        if self.stack[-1] == self.max[-1]:
            self.max.pop()            
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMax(self):
        return self.max[-1]


## Example Execution ##
stack = MaxStack()
stack.push(11)
stack.push(2)
stack.pop()
stack.push(16)
stack.pop()
stack.push(5)


result_top = stack.top()
print("Top Value:", result_top)

result_max = stack.getMax()
print("Maximum Value in Stack:", result_max)
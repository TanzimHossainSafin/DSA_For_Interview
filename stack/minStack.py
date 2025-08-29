class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStackVal=0
    def push(self, val: int) -> None:
     if len(self.stack) == 0:
        self.minStackVal = val
     elif val < self.minStackVal:
        self.minStackVal = val
     self.stack.append(val)
    def pop(self) -> None:
       if len(self.stack)>0:
          self.stack.pop()
       else:
          return None

    def top(self) -> int:
        if len(self.stack)>0:
          return self.stack[len(self.stack)-1]
        else:
           return  None

    def getMin(self) -> int:
        if len(self.stack)>0:
           return self.minStackVal
        else:
           return None
# Your MinStack object will be instantiated and called as such:
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]
obj=MinStack()
obj.push(-2)
obj.push(-4)
obj.push(-3)
#obj.pop()
print(obj.stack)
param_3 = obj.top()
print("top is",param_3)
param_4 = obj.getMin()
print("minimum is",param_4)
# Output
# [null,null,null,null,-3,null,0,-2]
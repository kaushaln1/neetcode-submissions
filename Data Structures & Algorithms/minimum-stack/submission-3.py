class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = float('inf')

    def push(self, val: int) -> None:
        currentMin = val if len(self.stack) ==0  else min(val,self.stack[-1][1]) 
        self.stack.append((val, currentMin))



    def pop(self) -> None:
        if len(self.stack) != 0:
            del self.stack[-1]
        

    def top(self) -> int:
        if len(self.stack) !=0 :
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        

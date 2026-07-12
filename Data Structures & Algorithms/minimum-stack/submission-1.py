class MinStack:

    def __init__(self):
        self.stk=[]
        self.min = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.min.append(min(val,self.min[-1] if self.min else val))

    def pop(self) -> None:
        self.min.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        

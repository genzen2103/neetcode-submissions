class MinStack:

    def __init__(self):
        self.temp = []
        self.current_min = 2**31
        
    def push(self, val: int) -> None:
        self.temp.append(val)
        if val < self.current_min:
            self.current_min = val

    def pop(self) -> None:
        top_val = self.temp.pop()
        if self.current_min == top_val:
            if len(self.temp)==0:
                self.current_min = 2**31
            else:
                self.current_min = min(self.temp)
        

    def top(self) -> int:
        return self.temp[-1]

    def getMin(self) -> int:
        return self.current_min
        

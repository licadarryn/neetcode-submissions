class MinStack:

    def __init__(self):
        self.s = []
        self.s_min = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.s_min:
            self.s_min.append(min(val, self.s_min[-1]))
        else:
            self.s_min.append(val)
        

    def pop(self) -> None:
        self.s.pop()
        self.s_min.pop()

        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.s_min[-1]
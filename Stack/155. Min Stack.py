################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/min-stack/
################################################################



class MinStack:

    def __init__(self):
        self.vals = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.vals.append(val)
        curMin = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(curMin)
        

    def pop(self) -> None:
        self.vals.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
    
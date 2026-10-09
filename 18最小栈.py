"""
设计一个支持 push实现 MinStack 类:

MinStack()初始化堆栈对象。
void push(int value)将元素 value 推入堆栈。
void pop()删除堆栈顶部的元素。
int top()获取堆栈顶部的元素。
int getMin()获取堆栈中的最小元素。。
"""
#列表的最后一个元素就是栈顶
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        #注意是小于等于
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
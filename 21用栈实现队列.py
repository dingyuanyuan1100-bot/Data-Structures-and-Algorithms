"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作(push、pop、
peek. empty):

实现 MyQueue 类:

· void push(int x)将元素x推到队列的末尾

· int pop()从队列的开头移除并返回元素

·int peek()返回队列开头的元素

· boolean empty()如果队列为空,返回true;否则,返回 false

说明:

· 你只能 使用标准的栈操作 -- 也就是只有 push to top,peek/pop from top,size,和 is
empty 操作是合法的。

· 你所使用的语言也许不支持栈。你可以使用list或者deque(双端队列)来模拟一个栈,只要是
标准的栈操作即可。
"""
class MyQueue:
    def __init__(self):
        self.queue_in = []
        self.queue_out = []

    def push(self,x):
        self.queue_in.append(x)
    def pop(self):
        return self.queue_out.pop()
    def peek(self):
        if not self.queue_out:
            while self.queue_in:
                self.queue_out.append(self.queue_in.pop())
    def empty(self):
        return len(self.queue_in) == 0

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.A = Queue()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.A.push(x)
        for i in xrange(self.A.size() - 1):
            self.A.push(self.A.pop())
    # @return nothing
    def pop(self):
        self.A.pop()

    # @return an integer
    def top(self):
        return self.A.peek()

    # @return an boolean
    def empty(self):
        return self.A.empty()
        
class Queue:
    """自制队列"""
    def __init__(self):
        self.A = collections.deque()
    
    def push(self,x):
        self.A.append(x)
        
    def peek(self):
        if len(self.A) != 0:
            return self.A[0]
    def pop(self):
        if len(self.A) != 0:
            temp = self.peek()
            del self.A[0]
            return temp
    
    def empty(self):
        return len(self.A) == 0
        
    def size(self):
        return len(self.A)
        
        
        
        

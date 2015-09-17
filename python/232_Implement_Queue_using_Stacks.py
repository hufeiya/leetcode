class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.A = Stack()
        self.B = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.A.push(x)

    # @return nothing
    def pop(self):
        self.peek()
        self.B.pop()

    # @return an integer
    def peek(self):
        if self.B.isEmpty():
            while not self.A.isEmpty():
                self.B.push(self.A.pop())
        return self.B.peek()

    # @return an boolean
    def empty(self):
        return self.A.isEmpty() and self.B.isEmpty()
            
  
class Stack: 
    """模拟栈""" 
    def __init__(self): 
        self.items = [] 
         
    def isEmpty(self): 
        return len(self.items)==0  
     
    def push(self, item): 
        self.items.append(item) 
     
    def pop(self): 
        return self.items.pop()  
     
    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 
         
    def size(self): 
        return len(self.items)        

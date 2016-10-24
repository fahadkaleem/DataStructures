class Stack(object):
    def __init__(self,limit = 10):
        self.stack_list = []
        self.limit = limit

    def is_empty(self):
        return len(self.stack_list)<=0

    def push(self,data):
        if len(self.stack_list)<=self.limit:
            self.stack_list.append(data)
            print('Stack:%s'%self.stack_list)
        else:
            print("Stack Overflow")

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            deletedElement = self.stack_list.pop()
            return deletedElement

    def peek(self):
        if self.isEmpty():
            return 0
        else:
            self.stack_list[len(self.stack_list)-1]

    def size(self):
        return len(self.stack_list)

    def isEmpty(self):
        if len(self.stack_list)<=0:
            print("Stack is empty")
            return True
        return False

ss = Stack()
ss.pop()
ss.push(1)
ss.push(2)
ss.push(5)
print(ss.size())
print(ss.pop())
print(ss.size())
class Stack:
    #Stack implementation as a list.

    def __init__(self):
        self._items = []  #new stack

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        self._items.pop()

    def peek(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)

s = Stack()
print(s.is_empty())
s.push('Olu')
print(s.is_empty())
print(s.peek())
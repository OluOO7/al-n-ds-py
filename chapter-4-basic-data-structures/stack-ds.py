class Stack:
    #Stack implementation as a list.

    def __init__(self):
        self._items = []  #new stack

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
         self._items.append(item)
    
    def pop(self):
         return self._items.pop()

    def peek(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)

"""
s = Stack()
print(s.is_empty())
s.push('Olu')
print(s.is_empty())
print(s.peek())
print(s.size())
s.push([1 ,2, 5])
print(s.size())
print(s)
print(s.pop())
print(s.size())
"""

#Function below uses Stack to reverse the characters in a string
def rev_string(my_str):
    my_str_stack = Stack()
    for i in my_str:
        my_str_stack.push(i)
        print(my_str_stack.peek())
    reversed_string = ""
    while not my_str_stack.is_empty():
        reversed_string += my_str_stack.pop()
    return print(reversed_string)
rev_string('I want an apple')

from stackDS import Stack

def decToBin(n):
    binDigit = ""
    binStack = Stack()
    q = n // 2
    binStack.push(n % 2)
    
    while(q > 0):
        binStack.push(q % 2)
        q //= 2
    print(binStack.size())
    
    while (binStack.is_empty() == False):
        binDigit += str(binStack.pop())
    return print(binDigit)

decToBin(235)

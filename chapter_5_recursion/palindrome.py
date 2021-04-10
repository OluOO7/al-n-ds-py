from 'C:\Users\Oluwaseun Olusanya\OneDrive\Desktop\Programming-Toolkits\Algorithms-and-Data-Structures\al-n-ds-py\chapter_4_basic_data_structures.stackDS' import Stack
def palindromer(s):
    new_string_stack = Stack()
    new_string =""
    
    for l in s:
        new_string_stack.push(l)
    
    while (new_string_stack.is_empty() == False):
        new_string += str(new_string_stack.pop())
    
    return print(new_string)

palindromer(kaya)  

'''Define two functions, one O(n**2) and the other O(n) that returns the minimum number in a list of number.
'''
import time

def findmin_quad(l):
    """
    Quadratic function that finds minimum number of a list.
    """
    start = time.time() 
    min_num = l[0]
    for i in l:
        ismin = True                #Assumes i is the minimum.
        for j in l:
            if i > j:               #Checks if indeed i is the minimum.
                ismin = False   
        if ismin:
            min_num = i
    end = time.time()  
    return min_num , end - start          
    
print(findmin_quad([10,2,3,-4,1,9,-8]))
'''Define two functions, one O(n**2) and the other O(n) that returns the minimum number in a list of number.
'''
def findmin(l):
    min_num = l[0]
    for i in l:
        ismin = True                #Assumes i is the minimum.
        for j in l:
            if i > j:               #Checks if indeed i is the minimum.
                ismin = False   
        if ismin:
            min_num = i
    return min_num            
    
print(findmin([10,2,3,-4,1,9]))
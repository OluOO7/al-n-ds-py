# Benchmarking a function to compute actual execution time.

import time
'''
def sum_of_n(n):
    start = time.time()  #start time

    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i

    end = time.time()    #end time

    return the_sum, end - start

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n(10000))
'''
def sum_of_n_2(n):
    start = time.time()
    
    result = (n * (n + 1)) / 2

    end = time.time()

    return result, end - start

for i in range(5):
    print("Sum is %d required %10.10f seconds" % sum_of_n_2(10000))
    print("Sum is %d required %10.10f seconds" % sum_of_n_2(100000))
    print("Sum is %d required %10.10f seconds" % sum_of_n_2(1000000))
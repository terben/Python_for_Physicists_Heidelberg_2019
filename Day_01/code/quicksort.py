#!/usr/bin/env python3

"""quicksort implementation from Wikipedia"""

# demonstration for Python code-readability
import random

# A python implementation of the Wikipedia quicksort algorithm
def my_quicksort(array):
    if len(array) < 1:
        return array
    
    pivot = array[0] # select a pivot
    rest = array[1:] # the array with the pivot
                     # removed
    less = [x for x in rest if x <= pivot]
    greater = [x for x in rest if x > pivot]
    
    return my_quicksort(less) + [pivot] + my_quicksort(greater)

# get 30 random integer numbers:
testarr = [ random.randint(-10000, 10000) for i in range(30) ]
print(testarr)
print(my_quicksort(testarr))

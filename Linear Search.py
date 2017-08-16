# Linear Search on a sorted array
# Complexity O(N)
# Description: Given a sorted array, the algorithm compares each element of the array with the inputted value in order to find a match.

import timeit

# search through a sorted array linear
def linearSearch(array, value):
    for elem in range(len(array)):
        if value == array[elem]:
            return "The number is ", array[elem], " at position ", elem
    return "No such number was found!"

# wrapper used for measuring the time it takes for the function to operate
def wrapper(function, *args, **kwargs):
    def wrapped():
        return function(*args, **kwargs)
    return wrapped

# testing
array = []
array.extend(range(1, 1000000))
try:
    input_value = int(input("Enter the number: "))
    print ("You entered: ", input_value)
    # do the binary search in the array
    print (linearSearch(array, input_value))
except ValueError:
    print ("You did not enter a number!")

# measure the time
wrapped = wrapper(linearSearch, array, input_value)
print(timeit.timeit(wrapped, number=100000))
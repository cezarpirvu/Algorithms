# Binary Search on a sorted array
# Complexity O(logN)
# Description: Binary search is an efficient algorithm for finding an item from an ordered list of items.
# It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

import timeit

# binary search in sorted array
def binarySearchArray(array, value):
    if array is None:
        raise ValueError("The array does not contain any elements!")

    # keep the min and the max boundaries of the search
    minBound = 0
    maxBound = len(array) - 1
    # // means floor division (cuts the part after the period)
    average = (maxBound + minBound) // 2

    # search for the number position in the array
    while maxBound >= minBound:
        if value == array[average]:
            return "The number is ", array[average], " at position ", average
        if value < array[average]:
            maxBound = average - 1
            average = (maxBound + minBound) // 2
        elif value > array[average]:
            minBound = average + 1
            average = (maxBound + minBound) // 2

    return "No such number found!"

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
    print (binarySearchArray(array, input_value))
except ValueError:
    print ("You did not enter a number!")

# measure the time
wrapped = wrapper(binarySearchArray, array, input_value)
print(timeit.timeit(wrapped, number=100000))
# Insertion sort on an unsorted array
# Complexity - O(N^2) worst case (when the array is reverse sorted already) except the one that needs to be introduced
#            - O(N) best case (when the array is already sorted) except the one that needs to be introduced
# Description: Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

import timeit

# insert a value into an array starting from an rightIndex
def insertValue(array, rightIndex, value):
    while rightIndex >= 0 and array[rightIndex] > value:
        array[rightIndex + 1] = array[rightIndex]
        rightIndex -= 1

    array[rightIndex + 1] = value

# sort an array using insertion sort
def insertionSort(array):
    if array is None:
        return "The array is null!"

    for i in range(1, len(array)):
        insertValue(array, i-1, array[i])

# wrapper used for measuring the time it takes for the function to operate
def wrapper(function, *args):
    def wrapped():
        return function(*args)

    return wrapped

# testing
array = [23, 22, 36, 1, 0, -24, 1, -29, 22, 54, 10]
insertionSort(array)
print(array)

# measure the time
wrapped = wrapper(insertionSort, array)
print(timeit.timeit(wrapped, number=100000))
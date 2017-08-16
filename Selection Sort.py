# Selection sort on an unsorted array
# Complexity O(N^2)
# Description: Compares the first element with the minimum element extracted from the remaining elements of the array. Afterwards, it swappes it if necessary.

import timeit

# swap two elements of an array
def swapArrayValue(array, index1, index2):
    aux = array[index1]
    array[index1] = array[index2]
    array[index2] = aux

# find the minimum index in an array
def findMinimumIndex(array, startingIndex):
    minIndex = startingIndex
    for i in range(startingIndex + 1, len(array)):
        if array[minIndex] > array[i]:
            minIndex = i
    return minIndex

# sort an array using selection sort
def selectionSort(array):
    if array is None:
        return "The array is null!"

    for i in range(0, len(array) - 1):
        minIndex = findMinimumIndex(array, i)
        swapArrayValue(array, i, minIndex)

# wrapper used for measuring the time it takes for the function to operate
def wrapper(function, *args):
    def wrapped():
        return function(*args)

    return wrapped

# testing
array = [23, 22, 36, 1, 0, -24, 1, -29, 22, 54, 10]
selectionSort(array)
print(array)

# measure the time
wrapped = wrapper(selectionSort, array)
print(timeit.timeit(wrapped, number=100000))

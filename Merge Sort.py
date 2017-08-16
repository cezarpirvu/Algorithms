# Merge sort on an unsorted array
# Complexity O(NlogN)
# Description Divide by finding the number q of the position midway between p and r.
# Do this step the same way we found the midpoint in binary search: add p and r, divide by 2, and round down.
# Conquer by recursively sorting the subarrays in each of the two subproblems created by the divide step.
# That is, recursively sort the subarray array[p..q] and recursively sort the subarray array[q+1..r].
# Combine by merging the two sorted subarrays back into the single sorted subarray array[p..r].

import timeit

# combine the values by merging the arrays
def merge(array, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

# divide the problem and afterwards combine
def mergeSort(array):

    if len(array) > 1:
        center = len(array) // 2
        left = array[:center]
        right = array[center:]

        mergeSort(left)
        mergeSort(right)
        merge(array, left, right)

# wrapper used for measuring the time it takes for the function to operate
def wrapper(function, *args):
    def wrapped():
        return function(*args)

    return wrapped

# testing
array = [23, 22, 36, 1, 0, -24, 1, -29, 22, 54, 10]
mergeSort(array)
print(array)

# measure the time
wrapped = wrapper(mergeSort, array)
print(timeit.timeit(wrapped, number=100000))
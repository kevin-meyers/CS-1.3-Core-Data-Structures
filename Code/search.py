#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None

    if item == array[index]:
        return index

    return linear_search_recursive(array, item, index=index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    length = len(array)
    if length == 0:
        return None

    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right - left) // 2 + left
        middle_item = array[middle]

        if item > middle_item:
            left = middle + 1

        elif item < middle_item:
            right = middle - 1

        else:
            return middle


def binary_search_recursive(array, item, left=None, right=None):
    if left is None: # consider a helper function
        left = 0
        right = len(array) - 1

    if left > right:
        return None

    middle = (right - left) // 2 + left
    middle_item = array[middle]

    if item == middle_item:
        return middle

    if item > middle_item:
        return binary_search_recursive(array, item, left=middle+1, right=right)

    return binary_search_recursive(array, item, left=left, right=middle-1)

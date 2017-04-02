#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests


    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Check if array is none:
    if array is None:
        return None
    # If item is not in the array:
    if index >= len(array):
        return None
    # Found item:
    if array[index] == item:
        return index
    else:
        # Go to next index:
        index += 1
        return linear_search_recursive(array, item, index)
    return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):

    list = sorted(array)
    upper = len(list)
    lower = 0
    half = (upper + lower) / 2

    while lower < upper:
        if array[half] == item:
            return half
        elif array[half] > item:
            upper = half
        else:
            # Check if this is the end of the array:
            if lower == half:
                return None
            lower = half
        half = (upper + lower) / 2
    return None

def binary_search_recursive(array, item, left=None, right=None):
    if left is None and right is None:
        array = sorted(array)
        right = len(array)
        left = 0
    half = (right + left) / 2
    if left >= right:
        return None
    if array[half] == item:
        return half
    elif array[half] > item:
        right = half
    else:
        # Check if this is the end of the array:
        if left == half:
            return None
        left = half
    return binary_search_recursive(array, item, left, right)

#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if array[index] == item:
        return index
    else:
        index += 1
        return linear_search_recursive(array, item, index)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        try:
            mid = (high + low) // 2
            if mid < array.index(item):
                low = mid + 1

            elif mid > array.index(item):
                high = mid - 1

            else:
                return mid
        except ValueError:
            return None


def binary_search_recursive(array, item, left=None, right=None):
    if left is None or right is None:
        left = 0
        right = len(array) - 1

    if left or right == len(array):
        return None
    mid = (left+right)//2
    if array.index(item) == mid:
        return mid
    elif array.index(item) > mid:
        left = mid + 1
    else:
        right = mid - 1

    if mid == (left + right) // 2:
        return None
    else:
        return binary_search_recursive(array, item, left, right)


print(binary_search_iterative(['fuck', 'this', 'stupid', 'shit'], "fudge"))

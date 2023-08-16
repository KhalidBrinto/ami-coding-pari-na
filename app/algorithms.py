# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return True

        elif array[mid] > x:
            low = mid + 1

        else:
            high = mid - 1

    return False


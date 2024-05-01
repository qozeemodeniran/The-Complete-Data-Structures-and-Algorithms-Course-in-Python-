"""Missing Number Write a function to find the missing number in a given integer array of 1 to 100. The function
takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find
missing number from 1 to 6 the second parameter will be 6.

Example

missing_number([1, 2, 3, 4, 6], 6) # 5
"""


def missing_numbers(arr, n):
    # the missing number can be found by subtracting the sum of array from the sum of the first n natural numbers in the array

    # calculate the sum of the first n natural terms
    total = n * (n + 1) // 2

    # calculate the sum of all numbers in the array
    arr_sum = sum(arr)

    # find the missing number by subtracting sum of array from sum of first natural  terms of the array
    missing_number = total - arr_sum

    return missing_number


print(missing_numbers([1, 2, 3, 4, 5, 6, 8, 9], 9))

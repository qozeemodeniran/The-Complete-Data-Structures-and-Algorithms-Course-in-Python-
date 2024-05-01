"""
Max Product of Two Integers
Find the maximum product of two integers in an array where all elements are positive.
Example
arr = [1, 7, 3, 4, 9, 5]
max_product(arr) # Output: 63 (9*7)
"""

def MaxProduct(arr):
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1 * max2

print(f"The maximum product of two integers in the array {[1, 7, 3, 4, 9, 5]} is {MaxProduct([1, 7, 3, 4, 9, 5])}")

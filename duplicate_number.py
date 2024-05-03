"""
Duplicate Number
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
"""

def remove_duplicates(arr):
    seen = []
    for num in arr:
        if num not in seen:
            seen.append(num)
        elif num in seen:
            continue

    return seen

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

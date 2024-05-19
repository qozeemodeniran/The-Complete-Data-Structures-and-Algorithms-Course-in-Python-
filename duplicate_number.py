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

"""
SOLUTION - Time and Space Complexity of Duplicate Number
def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]
Explanation:

Create an empty list unique_lst to store the unique elements, and an empty set seen to keep track of the elements already processed.

Iterate through the input list lst using a for loop.

For each item in lst, check if it is not in seen. If it's not in seen, append it to unique_lst and add it to the seen set.

Return the unique_lst containing the unique elements from the input list lst.

Time complexity analysis:

Creating an empty list unique_lst: O(1)

Creating an empty set seen: O(1)

Looping through the input list lst of length n: O(n)

For each item, checking if the item is in the set seen: O(1) on average

If the item is not in the set, appending it to the list unique_lst: O(1) on average

Adding the item to the set seen: O(1) on average

Returning the list unique_lst: O(1)

Overall time complexity: O(n)

The loop iterates through the entire list once, and the set operations (lookup, add) inside the loop have an average time complexity of O(1). Therefore, the overall time complexity is O(n).

Space complexity:

O(n), as we're using additional data structures (list and set) to store unique elements.
"""
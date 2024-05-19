"""
Conditional Filter
Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
Output:

{'b': 2, 'd': 4}
"""


def filter_dict(my_dict, condition):

    filter = {k: v for k, v in my_dict.items() if condition(k, v)}

    return filter


"""
SOLUTION - Time and Space Complexity of Conditional Filter
def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}


Explanation:

Use dictionary comprehension to create a new dictionary by iterating through the key-value pairs in the input dictionary my_dict using the items() method. The items() method returns an iterable that produces key-value pairs as tuples.

For each key-value pair (k, v) from the input dictionary, the dictionary comprehension checks if the condition is met by calling the condition(k, v) function. The condition function takes a key and a value as arguments and returns a boolean value.

If the condition is met, the dictionary comprehension creates a new entry in the filtered dictionary with the same key-value pair. The syntax is {k: v for k, v in my_dict.items() if condition(k, v)}.

The time complexity of this operation is O(n), where n is the number of elements in the dictionary my_dict. The dictionary comprehension iterates through all the key-value pairs in the input dictionary once.

Return the new dictionary containing the filtered key-value pairs.

Time complexity:

The overall time complexity of this function is O(n), where n is the number of elements in the dictionary my_dict. This is determined by the dictionary comprehension, which iterates through all the key-value pairs in the input dictionary.

Space complexity:

The space complexity of this function depends on the number of elements in the filtered dictionary, which in turn depends on the condition function. In the worst case, when all key-value pairs meet the condition, the space complexity is O(n), where n is the number of elements in the dictionary my_dict. In the best case, when no key-value pairs meet the condition, the space complexity is O(1) as the function creates an empty dictionary.
"""
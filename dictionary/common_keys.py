"""
Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}
"""


def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]

    return dict1

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))

"""
SOLUTION - Time and Space Complexity of Common Keys
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


This code snippet defines a function merge_dicts(dict1, dict2) that merges two dictionaries and sums the values of common keys.

Explanation:

Create a copy of dict1 named result. This ensures that the original dict1 is not modified during the process. The copy() method takes O(n) time complexity, where n is the number of elements in dict1. The space complexity is also O(n) as a new dictionary is created with the same number of elements as dict1.

Iterate through the key-value pairs of dict2 using a for loop. This loop runs for m iterations, where m is the number of elements in dict2. For each key-value pair:

a. Use the get() method to retrieve the current value associated with the key in the result dictionary. If the key is not present in result, get() returns the default value (0).

b. Add the value from dict2 to the current value (or 0, if the key is not in result) and update the result dictionary with the new value for the key. The get() and update operations take O(1) average time complexity.

Return the merged dictionary result.

Time complexity:

The overall time complexity of this function is O(n + m), where n is the number of elements in dict1 and m is the number of elements in dict2. The copy() method takes O(n) time, and the loop iterates m times with O(1) operations inside the loop.

Space complexity:

The space complexity of this function is O(n + m) in the worst case, where all keys in dict1 and dict2 are distinct, and the merged dictionary has n + m elements. In the best case, where dict1 and dict2 have the same keys, the space complexity is O(n) (or O(m), whichever is larger), as the merged dictionary has the same number of elements as the input dictionaries.
"""
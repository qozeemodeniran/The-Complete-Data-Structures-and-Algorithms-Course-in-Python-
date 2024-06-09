"""
SOLUTION - Time and Space Complexity of Elementwise Sum
SOLUTION 1

def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")

    result = tuple(a + b for a, b in zip(t1, t2))
    return result
Explanation

def tuple_elementwise_sum(t1, t2): - Define a function called "tuple_elementwise_sum" that takes two tuples "t1" and "t2" as arguments.

if len(t1) != len(t2): - Check if the lengths of the input tuples are not equal.

raise ValueError("Input tuples must have the same length.") - If the lengths of the tuples are not equal, raise a ValueError with a descriptive message.

result = tuple(a + b for a, b in zip(t1, t2)) - Use the zip function to pair corresponding elements of the input tuples, then use a generator expression to compute the element-wise sum, and finally pass the generator expression to the tuple constructor to create a new tuple with the sums.

return result - Return the resulting tuple containing the element-wise sums.

Time and Space Complexity

if len(t1) != len(t2): - Constant time complexity O(1) for checking the lengths of the tuples. Constant space complexity O(1) as it does not use any additional memory.

raise ValueError("Input tuples must have the same length.") - Constant time complexity O(1) for raising an exception. Constant space complexity O(1) for creating the exception object.

result = tuple(a + b for a, b in zip(t1, t2)) - Linear time complexity O(n), where n is the length of the input tuples, as it iterates through each pair of elements and computes the element-wise sum. Linear space complexity O(n) because it creates a new tuple with the same length as the input tuples to store the element-wise sums.

return result - Constant time complexity O(1) for returning the result. No additional space complexity.

Overall time complexity of the function is O(n) because it iterates through each pair of elements in the input tuples once. The overall space complexity is O(n) because the function creates a new tuple with the same length as the input tuples to store the element-wise sums.



SOLUTION 2

def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))
Explanation

def tuple_elementwise_sum(tuple1, tuple2): - Define a function called "tuple_elementwise_sum" that takes two tuples "tuple1" and "tuple2" as arguments.

return tuple(map(sum, zip(tuple1, tuple2))) - This line has multiple operations: a. zip(tuple1, tuple2) - Use the zip function to pair corresponding elements of the input tuples. The zip function returns an iterator over these pairs. b. map(sum, zip(tuple1, tuple2)) - Use the map function to apply the sum function to each pair of elements created by the zip function. The map function returns an iterator that applies the sum function to each pair, resulting in the element-wise sums. c. tuple(map(sum, zip(tuple1, tuple2))) - Pass the iterator returned by the map function to the tuple constructor to create a new tuple with the element-wise sums. d. return tuple(map(sum, zip(tuple1, tuple2))) - Return the resulting tuple containing the element-wise sums.

Time and Space Complexity

def tuple_elementwise_sum(tuple1, tuple2): - Define a function called "tuple_elementwise_sum" that takes two tuples "tuple1" and "tuple2" as arguments. No time or space complexity associated with this line as it is just a function definition.

return tuple(map(sum, zip(tuple1, tuple2))) - This line has multiple operations: a. zip(tuple1, tuple2) - The zip function has a linear time complexity O(n), where n is the length of the input tuples, as it iterates through each element in both input tuples to create pairs. The space complexity is also O(n) because it creates an iterator containing n pairs. b. map(sum, zip(tuple1, tuple2)) - The map function has a linear time complexity O(n), as it applies the sum function to each pair created by the zip function. The space complexity is O(n) because it creates an iterator containing n element-wise sums. c. tuple(map(sum, zip(tuple1, tuple2))) - The tuple constructor has a linear time complexity O(n) because it iterates through the iterator returned by the map function to create a new tuple. The space complexity is O(n) because it creates a new tuple with n element-wise sums.

The time complexities of the zip, map, and tuple operations are all linear, O(n), but they are combined in a single line, so the overall time complexity for this line is still O(n).

The overall time complexity of the function is O(n) because it iterates through each pair of elements in the input tuples once. The overall space complexity is O(n) because the function creates a new tuple with the same length as the input tuples to store the element-wise sums.
"""
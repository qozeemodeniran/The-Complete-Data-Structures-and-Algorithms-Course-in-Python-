"""
SOLUTION - Time and Space Complexity of Insert at the Beginning
def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple
Explanation

def insert_value_at_beginning(input_tuple, value_to_insert): - Define a function called "insert_value_at_beginning" that takes a tuple "input_tuple" and a value "value_to_insert" as arguments.

return (value_to_insert,) + input_tuple - Create a new tuple with the given value as the first element and concatenate the original tuple "input_tuple" to it. The comma after the value is necessary to create a single-element tuple. Return the new tuple.

Time and Space Complexity

def insert_value_at_beginning(input_tuple, value_to_insert): - Define a function called "insert_value_at_beginning" that takes a tuple "input_tuple" and a value "value_to_insert" as arguments. No time or space complexity associated with this line as it is just a function definition.

return (value_to_insert,) + input_tuple - This line creates a new tuple with the given value as the first element followed by the elements of the original tuple. The tuple concatenation operation has a linear time complexity O(n), where n is the length of the input tuple, as it creates a new tuple by copying the elements from the original tuple. The space complexity is also O(n) because it creates a new tuple with n+1 elements.

The overall time complexity of the function is O(n) because it iterates through the elements of the input tuple once to create a new tuple. The overall space complexity is O(n) because it creates a new tuple with n+1 elements.
"""
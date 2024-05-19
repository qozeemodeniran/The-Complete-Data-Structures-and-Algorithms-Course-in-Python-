"""
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]]

diagonal_sum(myList2D) # 15
"""
def DiagonalSum(matrix):
    principal = 0
    secondary = 0
    for i in range(0, len(matrix)):
        principal += matrix[i][i]
        secondary += matrix[i][len(matrix) - i - 1]

    return principal, secondary

myList2D = [[1,2,3],[4,5,6],[7,8,9]]
print(f"The principal and secondary diagonal sums in the 2x2 matrix {myList2D} is {DiagonalSum(myList2D)} respectfully")

"""
SOLUTION - Time and Space Complexity of 2D Lists


def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0
 
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
 
    return total
Explanation:

def diagonal_sum(matrix):

Define a function called diagonal_sum that takes a 2D list (matrix) as its argument.

total = 0

Initialize a variable 'total' to store the sum of the diagonal elements. Set its initial value to 0.

for i in range(len(matrix)):

Start a for loop that iterates through the range of the length of the matrix (number of rows). The index variable is 'i'.

total += matrix[i][i]

Add the value of the diagonal element at the current index to the 'total'. The diagonal element is the one where the row and column indices are the same (i.e., matrix[i][i]).

return total

After the for loop is done, return the total sum of the diagonal elements.

Time complexity:

O(n), where n is the number of rows (or columns) in the matrix. The function iterates through the rows once.

Space complexity:

O(1), as the function only uses a single variable to store the sum (total).


"""
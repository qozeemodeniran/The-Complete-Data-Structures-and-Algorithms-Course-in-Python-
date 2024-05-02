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
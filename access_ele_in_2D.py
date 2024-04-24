import numpy as np

twoDArray = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

def AccessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Invalid index")
    else:
        print(array[rowIndex][colIndex])

AccessElement(twoDArray, 0, 3)
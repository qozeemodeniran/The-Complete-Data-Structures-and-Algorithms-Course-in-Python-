import numpy as np

twoDArray = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(twoDArray)

def search2DArray(array, target):
    for r in range(len(array)):
        for c in range(len(array[0])):
            if array[r][c] == target:
                return f"The result of your search is located at row {r} column {c}"
    else:
        return f"Search not found"


print(search2DArray(twoDArray, 100))
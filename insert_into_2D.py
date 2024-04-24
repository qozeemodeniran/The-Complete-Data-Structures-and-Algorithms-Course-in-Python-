import numpy as np

twoDArray = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
# print(twoDArray)

# insert to start (or middle or anywhere else but not end!) of array
    # axix = 1 (inserts to column)
    # axis = 0 (inserts to row)
new2DArray  = np.insert(twoDArray, 0, [[0,1,0,1]], axis=1)
# print(new2DArray)
output = f"Inserting to any position other than end of the array\n{new2DArray}"
print(output)

# insert to end of an array
new2DArray  = np.append(twoDArray,[[0,1,0,1]], axis=0)
output = f"Inserting to the end of the array\n{new2DArray}"
print(output)

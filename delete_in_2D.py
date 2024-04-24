import numpy as np

twoDArray = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(twoDArray)

new2DArray = f"{np.delete(twoDArray, 0, axis=0)}"
print(new2DArray)

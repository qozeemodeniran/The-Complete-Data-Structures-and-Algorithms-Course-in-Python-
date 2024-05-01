"""
find the pair of numbers that sum up to a target in a given array: return the index of the pairs
"""
def FindPairs(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(i, j)
FindPairs([1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 4, 2, 12, 4], 7)
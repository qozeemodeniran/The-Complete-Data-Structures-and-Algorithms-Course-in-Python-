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

"""
SOLUTION - Time and Space Complexity of Pairs
def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result
 
arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']
Explanation:

def pairSum(arr, target_sum): - Define the function pairSum that takes the input array arr and the target sum target_sum as arguments.

result = [] - Initialize an empty list called result to store the pairs that add up to the target sum.

for i in range(len(arr)): - Start a loop iterating through the indices of the input array with the loop variable i.

for j in range(i+1, len(arr)): - Inside the outer loop, start another loop iterating through the indices of the input array starting from i+1 to avoid comparing an element with itself or repeating pairs. The loop variable is j.

if arr[i] + arr[j] == target_sum: - Check if the sum of the elements at index i and index j of the input array equals the target sum.

result.append(f"{arr[i]}+{arr[j]}") - If the sum of the elements at index i and index j equals the target sum, append a formatted string containing the pair to the result list.

return result - After iterating through all pairs in the array, return the result list containing the pairs that add up to the target sum.

arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9] - Define the input array for testing purposes.

target_sum = 7 - Define the target sum for testing purposes.

print(pairSum(arr, target_sum)) - Call the pairSum function with the input array and target sum, and print the resulting list of pairs.

Time and Space Complexity:

The time complexity of the pair_sum function is O(n^2), where n is the length of the input array arr. This is because the function uses nested loops, and for each element in the array, it checks every other element in the array for possible pairs.

The space complexity of the pair_sum function is O(n), where n is the length of the input array arr. The additional space used in this function is the result list, which stores the pairs that add up to the target sum. In the worst case, the number of pairs that sum up to the target value is proportional to the size of the input array.
"""
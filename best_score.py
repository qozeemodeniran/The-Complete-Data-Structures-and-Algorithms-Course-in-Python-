"""
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

"""


def first_second(my_list):
    first_best_score = 0
    second_best_score = 0
    for score in my_list:
        if score > first_best_score:
            second_best_score = first_best_score
            first_best_score = score
        elif score > second_best_score:
            second_best_score = score
    return first_best_score, second_best_score

print(first_second([84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]))

"""
SOLUTION - Time and Space Complexity of Best Score
def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
 
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
 
    return max1, max2
 
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)
Explanation:

Let me explain the code line by line:

def first_second(my_list):

Define a function called first_second that takes a list called my_list as an argument.

max1, max2 = float('-inf'), float('-inf')

Initialize two variables max1 and max2 to store the first and second best scores. Set their initial values to negative infinity.

for num in my_list:

Start a for loop that iterates through each element in my_list.

if num > max1:

Check if the current element is greater than max1.

max2 = max1

If the current element is greater than max1, update max2 to the current value of max1.

max1 = num

Set max1 to the current element, as it is now the highest value found so far.

elif num > max2 and num != max1:

If the current element is greater than max2 but not equal to max1, update max2.

max2 = num

Set max2 to the current element, as it is now the second-highest value found so far.

return max1, max2

After the for loop is done, return the first and second best scores as a tuple.

Time complexity:

The function iterates through the list my_list once, with each iteration taking constant time O(1) to perform comparisons and updates. Since there are n elements in the list, the overall time complexity of the function is O(n).

Space complexity:

The function uses a constant amount of additional space to store the variables max1 and max2. There are no other data structures or variables created that depend on the size of the input list. Therefore, the space complexity is O(1), as it remains constant regardless of the input size.
"""
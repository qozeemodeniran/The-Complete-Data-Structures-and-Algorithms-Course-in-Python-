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
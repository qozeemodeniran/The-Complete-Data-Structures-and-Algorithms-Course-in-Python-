orig_list = [-1, 10, -20, 2, -90, 60, 45, 20]

square_of_negatives = [number * number for number in orig_list if number < 0]
print(square_of_negatives)

no_of_days = int(input("How many day's average temprature do you wish to calcilate?: "))
temp_total = 0
for i in range(1, no_of_days+1):
    next_day = int(input(f"Day {i}'s highest temprature: "))
    temp_total += next_day

temp_avg = round(temp_total/no_of_days, 2)
print(f"The average temprature is {temp_avg}") 
no_of_days = int(input("How many day's average temprature do you wish to calcilate?: "))
temp_total = 0
temp_mem = []
for i in range(no_of_days):
    next_day = int(input(f"Day {i}'s highest temprature: "))
    temp_mem.append(next_day)
    temp_total += temp_mem[i]

temp_avg = round(temp_total/no_of_days, 2)
print(f"The average temprature is {temp_avg}") 

temp_above_avg = 0
for i in temp_mem:
    if i > temp_avg:
        temp_above_avg += 1
print(f"{temp_above_avg} day(s) is above average temprature")
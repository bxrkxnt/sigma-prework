input_arr = [3, -1, 5, 2, 0, 10]

min_num = 0
max_num = 0

for num in input_arr:
    if num < min_num:
        min_num = num

    if num > max_num:
        max_num = num

print(f"The min num is: {min_num}\nThe max num is: {max_num}")

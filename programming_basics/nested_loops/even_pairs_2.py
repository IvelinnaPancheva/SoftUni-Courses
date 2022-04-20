first_pair_lower_limit = int(input())
second_pair_lower_limit = int(input())
range_first_pair = int(input())
range_second_pair = int(input())

first_pair_upper_limit = first_pair_lower_limit + range_first_pair
second_pair_upper_limit = second_pair_lower_limit + range_second_pair
for x in range(first_pair_lower_limit, first_pair_upper_limit+1):
    x_counter = 0
    for m in range(1, x+1):
        if x % m == 0:
            x_counter += 1
            if x_counter > 2:
                break
    if x_counter == 2:
        for y in range(second_pair_lower_limit, second_pair_upper_limit+1):
            y_counter = 0
            for n in range(1, y+1):
                if y % n == 0:
                    y_counter +=1
                    if y_counter > 2:
                        break
            if y_counter == 2:
                left_pair = x
                right_pair = y
                print(f"{x}{y}")

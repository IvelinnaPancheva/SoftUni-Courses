n = int(input())
max_result = 0
max_weight = 0
max_time = 0
max_quality = 0

for i in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    snowball_result = int((weight / time) ** quality)
    if snowball_result > max_result:
        max_result = snowball_result
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_result} ({max_quality})")


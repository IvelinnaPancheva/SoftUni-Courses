n = int(input())

for x in range(1, n + 1):
	counter = 0
	for y in range(1, n + 1):
		if x % y == 0:
			counter += 1

	if counter == 2:
		print(x)
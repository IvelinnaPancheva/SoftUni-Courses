from collections import deque

petrol_pumps = deque()
n = int(input())

for i in range(n): # i = integer
    pump = [int(element) for element in input().split(" ")]
    petrol_pumps.append(pump)

for attempt in range(len(petrol_pumps)):
    petrol_in_tank = 0
    refill = petrol_pumps[0][0]
    distance = petrol_pumps[0][1]
    for i in range(len(petrol_pumps)):
        if petrol_in_tank + refill >= distance:
            petrol_in_tank += refill
            petrol_in_tank -= distance
        else: # petrol_in_tank + refill < distance
            break
    petrol_pumps.rotate(-1)

print()
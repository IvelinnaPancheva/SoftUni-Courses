from collections import deque

petrol_pumps = deque()
route = []
n = int(input())

for i in range(n): # i = integer
    pump = [int(element) for element in input().split(" ")]
    pump.append(i)
    petrol_pumps.append(pump)

petrol_in_tank = 0
while len(route) < len(petrol_pumps):
    refill = petrol_pumps[0][0]
    distance = petrol_pumps[0][1]
    number = petrol_pumps[0][2]
    if petrol_in_tank + refill >= distance:
        route.append(number)
        petrol_in_tank += refill
        petrol_in_tank -= distance
    else: # petrol_in_tank + refill < distance
        route = []
        petrol_in_tank = 0
    petrol_pumps.rotate(-1)

print(route[0])
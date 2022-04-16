steps_today = 0
target = 10000

while steps_today < target:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        steps_today += last_steps
        break
    else:
        current_steps = int(command)
        steps_today += current_steps

if steps_today >= 10000:
    diff = abs(steps_today - 10000)
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")

else:
    diff = abs(steps_today - 10000)
    print(f"{diff} more steps to reach goal.")
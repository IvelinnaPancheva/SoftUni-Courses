empl_happiness = input().split(" ")
factor = int(input())

empl_happiness = [int(num) * factor for num in empl_happiness]
average_happiness = sum(empl_happiness) / len(empl_happiness)
happy_employees = [x for x in empl_happiness if x >= average_happiness]
if len(happy_employees) >= len(empl_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(empl_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(empl_happiness)}. Employees are not happy!")
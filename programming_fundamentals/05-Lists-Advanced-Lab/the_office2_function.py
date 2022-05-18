def office_happiness(empl_happiness, factor):
    empl_happiness = list(map(lambda x: int(x) * factor, empl_happiness))
    average_happiness = sum(empl_happiness) / len(empl_happiness)
    happy_employees = list(map(lambda x: x if x >= average_happiness else "no", empl_happiness))
    happy_employees = list(filter(lambda x: x != "no", happy_employees))
    if len(happy_employees) >= len(empl_happiness) / 2:
        return f"Score: {len(happy_employees)}/{len(empl_happiness)}. Employees are happy!"
    else:
        return f"Score: {len(happy_employees)}/{len(empl_happiness)}. Employees are not happy!"


current_empl_happiness = input().split(" ")
current_factor = int(input())
print(office_happiness(current_empl_happiness, current_factor))


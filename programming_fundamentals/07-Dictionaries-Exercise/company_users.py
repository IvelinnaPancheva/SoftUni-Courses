data = input()
company_and_employees = {}

while not data == "End":
    split_data = data.split(" -> ")
    company = split_data[0]
    employee_id = split_data[1]

    if company not in company_and_employees:
        company_and_employees[company] = [employee_id]
    else:
        if employee_id not in company_and_employees[company]:
            company_and_employees[company].append(employee_id)

    data = input()

for company in company_and_employees:
    print(f"{company}")
    for employee in company_and_employees[company]:
        print(f"-- {employee}")
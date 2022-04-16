days = int(input())

treated = 0
untreated = 0
doctors = 7

for days in range(1, days + 1):
    patients = int(input())
    if days % 3 != 0:
        if doctors >= patients:
            treated += patients
        else: # doctors < patients
            untreated += (patients - doctors)
            treated += doctors

    else:  # days % 3 == 0:
        if untreated > treated:
            doctors += 1
        if doctors >= patients:
            treated += patients
        else: # doctors < patients
            untreated += (patients - doctors)
            treated += doctors

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
electrons = int(input())

n_shell = 1
filled_shells = []

while electrons >= 2 * (n_shell ** 2):
    current_electrons = 2 * (n_shell ** 2)
    filled_shells.append(current_electrons)
    electrons -= current_electrons
    n_shell += 1

if electrons == 0:
    print(filled_shells)
else:
    filled_shells.append(electrons)
    print(filled_shells)

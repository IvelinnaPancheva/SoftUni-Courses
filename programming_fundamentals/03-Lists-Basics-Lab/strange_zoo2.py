meerkat = list()
tail = meerkat.append(input())
body = meerkat.append(input())
head = meerkat.append(input())

temporary_variable = meerkat[0]
meerkat[0] = meerkat[2]
meerkat[2] = temporary_variable

print(meerkat)
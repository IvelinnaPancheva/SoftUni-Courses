meerkat = list()
tail = meerkat.append(input())
body = meerkat.append(input())
head = meerkat.append(input())

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)
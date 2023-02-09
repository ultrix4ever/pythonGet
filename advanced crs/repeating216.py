
a = input()


if len(a) == 5:
    print(int(a[::-1]))
else:
    a = int(a[0] + a[:-6:-1])
    print(a)
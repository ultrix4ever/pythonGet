n = int(input())
a, b, c = 1, 1, 1
if n == 1:
    print(a)
elif n == 2:
    print(a, b)
elif n == 3:
    print(a, b, c)
else:
    print(a, b, c, end=" ")

for i in range(n - 3):
    a, b, c = b, c, a + b + c
    print(c, end=" ")
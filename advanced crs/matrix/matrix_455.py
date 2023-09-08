n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    a[i][i], a[n - i - 1][i] = a[n - i - 1][i], a[i][i]

for row in a:
    print(*row)
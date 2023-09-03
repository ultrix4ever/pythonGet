n, m = int(input()), int(input())
a = []
for _ in range(n):
    b = map(int, input().split())
    a.append(list(b))
i, j = map(int, input().split())

for row in a:
    row[i], row[j] = row[j], row[i]

for row in a:
    print(*row)
n = int(input())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

a.reverse()

for row in a:
    print(*row)
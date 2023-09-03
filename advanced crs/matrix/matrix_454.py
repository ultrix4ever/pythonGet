n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            print('NO')
            exit()

print('YES')
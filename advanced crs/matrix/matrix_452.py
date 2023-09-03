
n = int(input())
m = int(input())
a = []
for _ in range(n):
    b = map(int,input().split())
    a.append(list(b))

max_value = a[0][0]
row = col = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > max_value:
            max_value = a[i][j]
            row = i
            col = j

print(row, col)

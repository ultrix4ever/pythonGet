L = input().split()
M = input().split()
new = []

for i in range(len(L)):
    new.append(int(L[i]) + int(M[i]))
print(*new)
m = int(input())
n = int(input())
HomeBooks = set()
NewBooks = set()

for i in range(m):
    HomeBooks.add(str(input()))

for i in range(n):
    if str(input()) in HomeBooks:
        print('YES')
    else:
        print('NO')
    
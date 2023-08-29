
num = int(input())
set1 = (1,2,3,4,5,6,7,8,9,0)
for i in range(num):
     set1 &= set([int(i) for i in input().split()])

print(*sorted(set1))


myset1 = set([i for i in input().split()])
myset2 = set([i for i in input().split()])

print(*(sorted(myset1 | myset2)))

print(*(sorted(set([i for i in input().split()]) | set([i for i in input().split()]))))
set1, set2, set3 = set([int(i) for i in input().split()]) , set([int(i) for i in input().split()]) , set([int(i) for i in input().split()])
set4 = set3 - set1 - set2
#print(set4)

print(*sorted(set4, reverse=True))
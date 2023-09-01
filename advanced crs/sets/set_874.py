set1, set2, set3 = set([int(i) for i in input().split()]) , set([int(i) for i in input().split()]) , set([int(i) for i in input().split()])
set4 = set1 | set2 | set3 
#print(set4)

set5 = set1 & set2 & set3
#print(set5)
print(*sorted(set4 ^ set5))
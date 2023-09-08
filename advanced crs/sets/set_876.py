set5 = set([1,2,3,4,5,6,7,8,9,0,10])
set1, set2, set3 = set([int(i) for i in input().split()]) , set([int(i) for i in input().split()]) , set([int(i) for i in input().split()])
set4 = set5 - set1 - set2 - set3 
#print(set4)

print(*sorted(set4))
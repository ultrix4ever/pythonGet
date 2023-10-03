myset1 = set([int(i) for i in input().split()])
myset2 = set([int(i) for i in input().split()])
myset3 = myset1 & myset2
if len(myset3) > 0:
    print(sorted(myset3, reverse=True))
else:
    print('BAD DAY') 
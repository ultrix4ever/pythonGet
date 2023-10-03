math = int(input())
inf = int(input())
NamesMath = set()
NamesInf = set()

for i in range(math):
    NamesMath.add(str(input()))

for i in range(inf):
    NamesInf.add(str(input()))

set3 = NamesMath ^ NamesInf
if len(set3) > 0:
    print(len(set3))
else:
    print('NO')
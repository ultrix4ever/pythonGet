math = int(input())
inf = int(input())
ListMathInf = []
SetMathInf = set()
for i in range(math+inf):
    ListMathInf.append(input())

for i in range(math+inf):
    if ListMathInf[i] not in SetMathInf:
        SetMathInf.add(ListMathInf[i])
    else:
        SetMathInf.discard(ListMathInf[i])

if len(SetMathInf) > 0:
    print(len(SetMathInf))
else:
    print('NO')

n = int(input())
list=[]

for _ in range(1, n+1):
    elem = [i for i in range(1, _+1)]
    list.append(elem)

print(*list, sep='\n')
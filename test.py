a = str(123456789)
lst = list(a)
lst2 = []

for i in range(-1,-len(a),-3):
    lst2 += lst[i:i-3:-1]+[',']
    print(lst2)
lst2 = lst2[::-1]
if lst2[0] == ',':
    print(*lst2[1:], sep='')
else: 
    print(*lst2, sep='')
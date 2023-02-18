count = int(input())
lst = []
for i in range(count):
    lst += [int(input())]
num = int(input())
Flag = False

for i in range(len(lst)):
    for j in range(i+1):
        if i != j and lst[i] * lst[j] == num:
            Flag = True

if Flag == False:
    print('НЕТ')
else:
    print('ДА')
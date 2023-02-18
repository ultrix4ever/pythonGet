
count1=0
count2=0
count3=0
count4=0
lst = []

for i in range(int(input())):
    xy = input()
    lst = xy.split()
    if int(lst[0]) > 0 and int(lst[1]) > 0:
        count1 +=1
    if int(lst[0]) < 0 and int(lst[1]) > 0:
        count2 +=1
    if int(lst[0]) < 0 and int(lst[1]) < 0:
        count3 +=1
    if int(lst[0]) > 0 and int(lst[1]) < 0:
        count4 +=1

print('Первая четверть:', count1)
print('Вторая четверть:', count2)
print('Третья четверть:', count3)
print('Четвертая четверть:', count4)
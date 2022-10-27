n = int(input())
list1 = []
list2 = []

for i in range(n):
    list3 = [int(i) for i in input().split()]
    list2 += list3
    
print(list2)
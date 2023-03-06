list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for i in range(len(list1)):
    total += sum(list1[i])
    counter += len(list1[i])

print(total/counter)
    
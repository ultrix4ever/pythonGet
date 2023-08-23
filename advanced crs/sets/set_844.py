numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
numbers = list(numbers)
#print(numbers)
fin_sum = 0
for i in range(len(numbers)):
    fin_sum += numbers[i]**2
#    print(numbers[i])
#    print(fin_sum)
print(fin_sum)
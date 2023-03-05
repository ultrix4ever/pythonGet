
lst = input().split()
count = 0
lst += 0

for i in range(len(lst)-1):
    if lst[i+1] > lst[i]:
        count += 1
print(count)
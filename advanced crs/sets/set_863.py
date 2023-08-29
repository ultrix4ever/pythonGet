
str1, str2 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
str3 = str1 - str2
print(*sorted(str3))


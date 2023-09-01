num = int(input())
my_str = ''
for i in range(num):
     my_str += input().lower()
unic_set = set(my_str)
print(len(unic_set))
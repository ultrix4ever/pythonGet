# my_str = input()
# count = 0
# list_c=[]
# for i in range(0, len(my_str)-1):
#     if my_str[i] == my_str[i+1] == 'Р':
#         count += 1
#     else:
#         list_c.append(count)
# print(max(list_c))

S=input()
t=0
while "Р"*(t+1) in S:
    t+=1
print(t)
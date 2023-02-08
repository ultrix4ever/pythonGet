#s = input()
#s = s.lower()
#sList = s.split()
s = input().lower().split()
counter = 0
counter += s.count('a')
counter += s.count('an')
counter += s.count('the')
print('Общее количество артиклей:', counter)
import random

n = int(input())    # количество попыток
list = ['Орел', 'Решка']

for i in range(n):  
    m = random.randrange(0,2)
    print(list[m])

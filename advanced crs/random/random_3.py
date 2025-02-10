import random

length = int(input())    # длина пароля

password1 = [random.randrange(65, 91) for i in range(length)]
password2 = [random.randrange(97, 123) for i in range(length)]  

for i in range(length):
    n = random.randrange(0, 2)
    if n == 0:
        print(chr(password1[i]), end='')
    else:
        print(chr(password2[i]), end='')




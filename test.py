def is_valid(num, x, y):
    if y < x:
        x, y = y, x
    if num in range(x, y) and x != y:
        return True
    else:
        return False

print('Добро пожаловать в числовую угадайку')
x = int(input('Ввездите первое число диапазона  '))
y = int(input('Ввездите второе число диапазона. Оно должно быть больше первого  '))
num = int(input('Ввездите число   '))

print(is_valid(num, x, y))
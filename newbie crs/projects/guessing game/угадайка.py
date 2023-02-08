import random

def guessing_game(x,y):
    num_random = random.randint(x,y)
    count = 0
    while True:
        num = int(input('Введите число  '))
        count += 1
        if is_valid(num, x, y) == True:
            if num < num_random:
                print('Слишком мало, попробуйте еще раз')          
            elif num > num_random:
                print('Слишком много, попробуйте еще раз')
            else:
                print('Вы угадали, поздравляем!', 'Колличество попыток =', count)
                break
        else:
            print('Число не из диапазона. Попробуй еще раз')            

def is_valid(num, x, y):
    if y < x:
        x, y = y, x
    if num in range(x,y) and x != y:
        return True
    else:
        return False

print('Добро пожаловать в числовую угадайку')
x = int(input('Ввездите первое число диапазона  '))
y = int(input('Ввездите второе число диапазона. Оно должно быть больше первого  '))

guessing_game(x,y)

while True:
    if input('Хотите сыграть еще раз  Да\Нет  ').lower() in ['да', 'lf']:
        print('Добро пожаловать в числовую угадайку')
        x = int(input('Ввездите первое число диапазона  '))
        y = int(input('Ввездите второе число диапазона. Оно должно быть больше первого  '))
        guessing_game(x,y)
    else:
        print('Сыграем в следующий раз! До встречи !')
        break
